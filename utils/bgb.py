import subprocess
from typing import Iterable

from constants import file_paths as files
from utils.movies import MovieContext


def call_bgb(in_save: str,
             out_save: str,
             breakpoint_list: Iterable[str],
             demo: str = None,
             movie_context: "MovieContext" = None, hf: bool = True, timeout: int = 10) -> None:
	subprocess.call([files.BGB_PATH, '-rom', in_save,
	                 *(['-br', ",".join(breakpoint_list)] if breakpoint_list else []),
	                 '-hf' if hf else '',
	                 '-nobatt',
	                 '-stateonexit', out_save,
	                 *(['-demoplay', demo] if demo else []),
	                 *([
		                   "-set", "RecordAVI=1",
		                   "-set", "WavFileOut=1",
		                   "-set", f"RecordAVIfourCC=cscd",
		                   "-set", "RecordHalfSpeed=0",
		                   "-set", "Speed=1",
		                   "-set",
		                   f"RecordPrefix={movie_context.movie_working_dir}/movie{movie_context.movie_index:05}",
	                   ] if movie_context is not None else []),
	                 ], timeout=timeout)