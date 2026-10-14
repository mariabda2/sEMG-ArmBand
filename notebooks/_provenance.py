"""Sello de procedencia para notebooks.

Uso:
    from _provenance import Sello
    sello = Sello('05_channel_fusion.ipynb')
    ...
    sello.mostrar()   # al final del notebook: crea/actualiza PROVENANCE.md
                      # en la raíz del repo y muestra el sello en los outputs

    sello.guardar()   # solo guarda sin mostrar
"""

import subprocess
from datetime import datetime
from pathlib import Path

DEFAULT_DIRS = ("data", "resultados", "figures")


def _repo_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / ".git").exists():
            return p
    return start


def _git(*args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if out.returncode == 0:
            return out.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        pass
    return None


class Sello:
    def __init__(self, notebook: str, dirs=DEFAULT_DIRS):
        self.notebook = notebook
        self.inicio = datetime.now()
        self.raiz = _repo_root(Path.cwd())

        self.commit = _git("-C", str(self.raiz), "rev-parse", "--short", "HEAD")
        self.rama = _git("-C", str(self.raiz), "rev-parse", "--abbrev-ref", "HEAD")
        status = _git("-C", str(self.raiz), "status", "--porcelain")
        if status is None:
            self.estado = "desconocido (git no disponible)"
        else:
            n = len(status.splitlines())
            self.estado = "limpio" if n == 0 else f"sucio ({n} archivos sin commitear)"

        self.dirs = [self.raiz / d for d in dirs]

    def registrar(self, path):
        """Registro manual opcional de un archivo de salida."""
        if not hasattr(self, "_manual"):
            self._manual = []
        self._manual.append(Path(path))

    def salidas(self):
        """Archivos generados desde la creación del sello (mtime >= inicio)."""
        encontrados = []
        for d in self.dirs:
            if not d.is_dir():
                continue
            for f in d.rglob("*"):
                if f.is_file() and datetime.fromtimestamp(f.stat().st_mtime) >= self.inicio:
                    encontrados.append(f)
        for f in getattr(self, "_manual", []):
            if f.exists() and f not in encontrados:
                encontrados.append(f)
        return sorted(encontrados)

    def markdown(self) -> str:
        lineas = [
            "### Sello de procedencia",
            "",
            "| Campo | Valor |",
            "|---|---|",
            f"| Notebook | `{self.notebook}` |",
            f"| Commit | `{self.commit or 'desconocido'}` |",
            f"| Rama | `{self.rama or 'desconocida'}` |",
            f"| Estado | {self.estado} |",
            f"| Ejecutado | {self.inicio.isoformat(timespec='seconds')} |",
        ]
        lineas += ["", "**Archivos generados en esta ejecución:**", ""]
        salidas = self.salidas()
        if salidas:
            rel = [str(f.relative_to(self.raiz)) for f in salidas]
            lineas += [f"- `{r}`" for r in rel]
        else:
            lineas.append("- (ninguno detectado en `data/`, `resultados/`, `figures/`)")
        return "\n".join(lineas)

    def _fila(self) -> str:
        rel = [f"`{f.relative_to(self.raiz)}`" for f in self.salidas()]
        archivos = "<br>".join(rel) if rel else "—"
        return (
            f"| `{self.notebook}` | `{self.commit or 'desconocido'}` "
            f"| `{self.rama or 'desconocida'}` | {self.estado} "
            f"| {self.inicio.isoformat(timespec='seconds')} | {archivos} |"
        )

    @staticmethod
    def _cabecera() -> list[str]:
        return [
            "# Procedencia de resultados",
            "",
            "> Documento generado automáticamente por `notebooks/_provenance.py`.",
            "> Cada ejecución de un notebook actualiza su propia fila. No editar manualmente.",
            "",
            "| Notebook | Commit | Rama | Estado | Ejecutado | Archivos generados |",
            "|---|---|---|---|---|---|",
        ]

    def guardar(self, path=None) -> Path:
        """Crea o actualiza PROVENANCE.md (upsert por nombre de notebook)."""
        path = Path(path) if path else self.raiz / "PROVENANCE.md"
        fila = self._fila()
        clave = f"| `{self.notebook}` |"

        if path.exists():
            lineas = path.read_text(encoding="utf-8").splitlines()
        else:
            lineas = self._cabecera()

        idx = next(
            (i for i, l in enumerate(lineas) if l.startswith("|") and l.startswith(clave)),
            None,
        )
        if idx is not None:
            lineas[idx] = fila
        elif any(l.startswith("| Notebook |") for l in lineas):
            # insertar después de la última fila de la tabla
            ultima = max(i for i, l in enumerate(lineas) if l.startswith("|"))
            lineas.insert(ultima + 1, fila)
        else:
            # archivo sin tabla: agregar la tabla completa al final
            lineas += [""] + self._cabecera() + [fila]

        path.write_text("\n".join(lineas) + "\n", encoding="utf-8")
        self.archivo = path
        return path

    def mostrar(self):
        from IPython.display import Markdown, display

        self.guardar()
        md = self.markdown() + f"\n\n> Guardado en `{self.archivo.name}` (raíz del repo)."
        display(Markdown(md))

    def __repr__(self):
        return (
            f"Sello(notebook={self.notebook!r}, commit={self.commit!r}, "
            f"rama={self.rama!r}, estado={self.estado!r}, "
            f"inicio={self.inicio.isoformat(timespec='seconds')})"
        )
