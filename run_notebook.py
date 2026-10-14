"""Run the versioned notebook as Python without a Jupyter server."""
import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    data_dir = args.data_dir.resolve()
    for name in ("train.csv", "test.csv", "sample_submission.csv"):
        if not (data_dir / name).is_file():
            parser.error(f"Missing {name} in {data_dir}")
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    notebook_path = Path(__file__).parent / "notebooks" / "Airline_Satisfaction_Kaggle_Starter.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    scope = {"__name__": "__notebook__"}
    first = True
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] != "code":
            continue
        source = cell["source"]
        if isinstance(source, list):
            source = "".join(source)
        print(f"Running code cell {index + 1}")
        exec(compile(source, f"{notebook_path}:cell-{index + 1}", "exec"), scope)
        if first:
            scope["DATA_DIR_OVERRIDE"] = str(data_dir)
            scope["OUTPUT"] = output_dir
            first = False
    print(f"Finished: {output_dir / 'submission.csv'}")

if __name__ == "__main__":
    main()
