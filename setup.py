from cx_Freeze import setup, Executable

executable = [Executable("main.py")]

setup(
    name = "Space_invaders",
    version = "1.0",
    description = "Space Invadres App",
    options = {"build_exe": {"packages": ["pygame"]}},
    executables = executable
)