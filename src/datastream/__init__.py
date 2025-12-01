from src.import_module import import_module

#
mod = import_module(__file__, "stream", "stream")
# mod=import_module(__file__, 'stream', 'stream_impl')
Stream = mod.Stream

from .main import main
