import os
import subprocess
from typing import Iterable

from constants import file_paths as files
from utils.movies import MovieContext

USE_WINE = False


def call_bgb(in_save: str,
             out_save: str,
             breakpoint_list: Iterable[str],
             demo: str = None,
             movie_context: "MovieContext" = None, hf: bool = True, timeout: int = 10) -> None:
	if in_save != out_save and os.path.exists(out_save):
		os.remove(out_save)


	bgb_arguments = [files.BGB_PATH, '-rom', in_save,
	                 *(['-br', ",".join(breakpoint_list)] if breakpoint_list else []),
	                 '-hf' if hf else '',
	                 '-nobatt',
	                 '-stateonexit', out_save,
	                 "-set", "CheatAutoSave=1",
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
	                 ]

	if USE_WINE:
		bgb_arguments = ["wine", *bgb_arguments]

	retries = 0
	return_code = subprocess.call(bgb_arguments, timeout=timeout)

	while return_code != 0 and retries < 3 and in_save != out_save:
		retries += 1
		return_code = subprocess.call(bgb_arguments, timeout=timeout)

	if return_code != 0:
		raise subprocess.CalledProcessError(return_code, " ".join(bgb_arguments))

	if movie_context is not None:
		movie_context.movie_index += 1
