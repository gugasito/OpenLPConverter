from cx_Freeze import setup, Executable

setup(
    name="OpenLPConverter",
    version="2.0",
    description="Convertimos archivos de OpenLP a archivos de ProPresenter",
    options={
        'build_exe': {
            'include_files': ['logo.png', 'logo.ico']
        }
    },
    executables=[Executable("OpenLPConverter.py", base="Win32GUI", icon="logo.ico")],
)
