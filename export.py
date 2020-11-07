import PyInstaller.__main__
import os

NAME = 'FreeFlowLearning'
BUILD_DIR = os.path.join(os.getcwd(), 'build')
DIST_PATH = os.path.join(os.getcwd(), 'binaries')


resource_args = [
    *['--add-binary=%s:.' % os.path.join(NAME, 'Frontend','static', 'img', file) for file in os.listdir(os.path.join(NAME, 'Frontend','static', 'img'))],
    
    *['--add-data=%s:.' % os.path.join(NAME, 'Frontend','static', 'js', file) for file in os.listdir(os.path.join(NAME, 'Frontend', 'static', 'js'))],
    
    *['--add-data=%s:.' % os.path.join(NAME, 'Frontend','templates', file) for file in os.listdir(os.path.join(NAME, 'Frontend','templates'))]
]



PyInstaller.__main__.run([
    '--name=%s' % NAME,
    '--onefile',
    '--log-level=CRITICAL',
    '--distpath=%s' % DIST_PATH,
    '--specpath=%s' % os.getcwd(),
    '--workpath=%s' % BUILD_DIR,
    *resource_args,
    os.path.join(NAME, '__main__.py'),
])

os.system('rm -rf %s' % BUILD_DIR)

os.remove('%s.spec' % NAME)