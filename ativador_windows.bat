chcp 65001
git init
set contagem=0

:a
python merdabot.py
set /a contagem+=1
if contagem==50 goto a

set contagem=0
git commit -a -m "segue a vida"
git push merdabot master
goto a