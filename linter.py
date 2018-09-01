from SublimeLinter.lint import Linter, util

class HexaLinter(Linter):
    tempfile_suffix = 'hexa'
    cmd = 'hexa --syntax-linter $temp_file'
    regex = r'^\[.+?:(?P<line>\d+):(?P<col>\d+)\]: (?P<message>.+?(?P<near>`.+`)?.+|$)'
    multiline = False
    line_col_base = (1,0)
    error_stream = util.STREAM_STDOUT
    defaults = {
        'selector': 'source.hexa'
    }

