import datetime
import pathlib

root = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    readme = root / "README.md"
    now = datetime.datetime.utcnow()
    md1 = f"[![StandWithUkraine]([![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)"
    #md2 = f"Today is {now.strftime('%B %d, %Y')} (UTC), and it's {}"
    readme.open("w").write(md1)
