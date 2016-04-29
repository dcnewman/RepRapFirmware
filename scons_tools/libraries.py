import os.path

build_libraries = {

#  directory name Libraries/ : [
#    Libraries/ | Duet/
#    [ directories with include files, None=just the library directory itself],
#    [ directories to build, None=all ],
#    [ directories to ignore, None=none ],
#    [ arduino library dependencies ]
#  ]

  'EMAC' : [ None, None, None, None, ['core'] ],
  'Fatfs' : [ 'Libraries', None, None, None, ['core'] ],
  'Flash' : [ 'Libraries', None, None, None, ['core'] ],
  'Lwip' : [ None, [ 'Lwip', 'Lwip/lwip/src/include' ], None,
             ['Lwip/lwip/src/core/ipv6', 'Lwip/lwip/test'], ['core'] ],
  'TemperatureSensor' : [ 'Libraries', None, None, None, ['core', 'SharedSpi'] ],
  'MCP4461' : [ 'Libraries', None, None, None, ['core', 'Wire'] ],
  'MCP4461-RADDS' : [ None, ['MCP4461'], ['MCP4461'], None, [ ] ]
}


# Recursive descent listing of a directory tree

def list_dirs(dir, ignore=None):
  if ignore is None:
    ignore = [ ]
  list = []
  for d in dir:
    subdirs = [ d + '/' + name for name in os.listdir(d) if os.path.isdir(os.path.join(d, name)) and \
                    (name[0] != '.') and (not (d + '/' + name) in ignore) ]
    list += list_dirs(subdirs, ignore)
  return dir + list

def get_lib_dirs(lib, variant = 'Duet'):

  if build_libraries[lib][0] is None:
    lpath = variant
  else:
    lpath = build_libraries[lib][0]

  idirs = build_libraries[lib][3]
  if not idirs is None:
    idirs = [os.path.join('..', '..', 'src', lpath, s) for s in idirs]
  else:
    idirs = [ ]

  if build_libraries[lib][2] == None:
    s = os.path.join('..', '..', 'src')
    tmp = list_dirs([os.path.join(s, lpath, lib) ], idirs)
    subdirs = []
    for sd in tmp:
      subdirs.append(sd.lstrip(s))
  else:
    subdirs = []
    for d in build_libraries[lib][2]:
      subdirs.append(os.path.join(lpath, d))

  subdirs.sort()

  if len(subdirs) == 0:
    subdirs = [ os.join('Libraries', lib) ]

  return subdirs

def append_path(paths, path):
  if not (path in paths):
    paths.append(path)

# Append to the list paths the strings
#
#     'Libraries/' + dirs[i]
#
# if dirs is None or '' then append just
#
#     'Libraries/' + dirname

def append_paths(paths, dirname, variant = 'Duet'):

  if (paths is None) or (dirname is None):
    return

  if build_libraries[dirname][0] is None:
    lpath = variant
  else:
    lpath = build_libraries[dirname][0]

  dirs = build_libraries[dirname][1]
  if (dirs is None) or (dirs == ''):
    append_path(paths, os.path.join(lpath, dirname))
  elif type(dirs) is str:
    append_path(paths, os.path.join(lpath, dirs))
  else:
    for d in dirs:
      append_path(paths, os.path.join(lpath, d))

def append_arduino_path(lib, paths, platform = 'duet', base = None):
  if (lib is None) or (paths is None):
    return

  if base is None:
    base = ''

  if lib == 'core':
    append_path(paths, os.path.join(base, 'cores', 'arduino'))
    append_path(paths, os.path.join(base, 'asf'))
    append_path(paths, os.path.join(base, 'asf', 'common', 'services', 'clock'))
    append_path(paths, os.path.join(base, 'asf', 'common', 'utils'))
    if platform == 'radds':
      append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'dmac'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'emac'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'efc'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'pmc'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'rstc'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'rtc'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'spi'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'drivers', 'twi'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'services', 'flash_efc'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'utils'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'utils', 'cmsis', 'sam3x', 'include'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'utils', 'header_files'))
    append_path(paths, os.path.join(base, 'asf', 'sam', 'utils', 'preprocessor'))
    append_path(paths, os.path.join(base, 'asf', 'thirdparty', 'CMSIS', 'Include'))
    append_path(paths, os.path.join(base, 'variants', 'duet'))
  else:
    append_path(paths, os.path.join(base, 'libraries', lib))
