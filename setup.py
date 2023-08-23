from glob import glob

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"

sources: list = sorted(glob("./JUCE/modules/**/*.cpp"))
include_dirs: list = ["./JUCE/modules/"]

ext_modules = [
    Pybind11Extension(
        "jucepy",
        sources,
        include_dirs,
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="jucepy",
    version=__version__,
    url="https://github.com/pat-ike-egb/jucepy",
    description="quick python bindings for juce using pybind11",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    python_requires=">=3.10",
)
