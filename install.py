fr=open('./play').read()
to=open('/usr/bin/pychess', 'w')
to.write(fr)
to.close()
