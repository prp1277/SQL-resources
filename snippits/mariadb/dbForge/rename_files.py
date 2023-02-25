import os

[os.rename(f, f.replace(".sql", ".xml")) for f in os.listdir(".") if not f.startswith(".")]
