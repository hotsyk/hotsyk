import datetime
import pathlib

root = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    readme = root / "README.md"
    now = datetime.datetime.utcnow()
    md = f"Hello there. Today is {now.strftime('%B %d, %Y')} (UTC)"
    readme.open("w").write(md)
