# Stubs for multiprocessing.managers

# NOTE: These are incomplete!

import queue
import threading
from typing import (
    Any, Callable, ContextManager, Dict, Iterable, Generic, List, Mapping, Optional,
    Sequence, Tuple, TypeVar, Union,
)

_T = TypeVar('_T')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class Namespace: ...

_Namespace = Namespace

class BaseProxy: ...

class ValueProxy(BaseProxy, Generic[_T]):
    def get(self) -> _T: ...
    def set(self, value: _T) -> None: ...
    value: _T

class BaseManager(ContextManager[BaseManager]):
    address: Union[str, Tuple[str, int]]
    def connect(self) -> None: ...
    @classmethod
    def register(cls, typeid: str, callable: Optional[Callable[..., Any]] = ...,
                 proxytype: Any = ...,
                 exposed: Optional[Sequence[str]] = ...,
                 method_to_typeid: Optional[Mapping[str, str]] = ...,
                 create_method: bool = ...) -> None: ...
    def shutdown(self) -> None: ...
    def start(self, initializer: Optional[Callable[..., Any]] = ...,
              initargs: Iterable[Any] = ...) -> None: ...

class SyncManager(BaseManager, ContextManager[SyncManager]):
    def BoundedSemaphore(self, value: Any = ...) -> threading.BoundedSemaphore: ...
    def Condition(self, lock: Any = ...) -> threading.Condition: ...
    def Event(self) -> threading.Event: ...
    def Lock(self) -> threading.Lock: ...
    def Namespace(self) -> _Namespace: ...
    def Queue(self, maxsize: int = ...) -> queue.Queue[Any]: ...
    def RLock(self) -> threading.RLock: ...
    def Semaphore(self, value: Any = ...) -> threading.Semaphore: ...
    def Array(self, typecode: Any, sequence: Sequence[_T]) -> Sequence[_T]: ...
    def Value(self, typecode: Any, value: _T) -> ValueProxy[_T]: ...
    def dict(self, sequence: Mapping[_KT, _VT] = ...) -> Dict[_KT, _VT]: ...
    def list(self, sequence: Sequence[_T] = ...) -> List[_T]: ...

class RemoteError(Exception): ...
