Remove-Item -Recurse -Force .\dist
Remove-Item -Recurse -Force .\build

$PATHS=$env:USERPROFILE + '\anaconda3\envs\comment_generator\Lib\site-packages'
pyinstaller.exe --onefile --paths=$PATHS ./comment_generator/main.py

copy .\config.toml .\dist
copy .\.env_local .\dist\.env
copy .\README.md .\dist

cd dist
Compress-Archive -Force * ..\comment_generator.zip
cd ..