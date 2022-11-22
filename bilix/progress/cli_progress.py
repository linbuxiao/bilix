from typing import Optional, Any
from rich.progress import Progress, TaskID, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn, \
    TimeRemainingColumn

from .base_progress import BaseProgress


class CLIProgress(BaseProgress):
    _progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        TextColumn("[progress.percentage]{task.percentage:>4.1f}%"),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        'ETA',
        TimeRemainingColumn(), transient=True
    )

    def __init__(self, holder=None):
        super().__init__(holder=holder)
        self._progress.start()  # ensure progress is start

    @classmethod
    def start(cls):
        cls._progress.start()

    @classmethod
    def stop(cls):
        cls._progress.stop()

    @property
    def tasks(self):
        return self._progress.tasks

    async def add_task(
            self,
            description: str,
            start: bool = True,
            total: Optional[float] = 100.0,
            completed: int = 0,
            visible: bool = True,
            **fields: Any,
    ) -> int:
        return self._progress.add_task(description=description, start=start, total=total, completed=completed,
                                       visible=visible, **fields)

    async def update(
            self,
            task_id: int,
            *,
            total: Optional[float] = None,
            completed: Optional[float] = None,
            advance: Optional[float] = None,
            description: Optional[str] = None,
            visible: Optional[bool] = None,
            refresh: bool = False,
            **fields: Any,
    ) -> None:
        return self._progress.update(TaskID(task_id), total=total, completed=completed, advance=advance,
                                     description=description, visible=visible, refresh=refresh, **fields)