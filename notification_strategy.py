from abc import ABC, abstractmethod

# Interfaz
class NotificationPolicy(ABC):
    @abstractmethod
    def should_notify(self, event: str) -> bool:
        pass

# Estrategia 1
class AlwaysNotify(NotificationPolicy):
    def should_notify(self, event: str) -> bool:
        return event in ["TASK_CREATED", "STATUS_CHANGED", "TASK_DONE"]

# Estrategia 2
class NotifyOnDoneOnly(NotificationPolicy):
    def should_notify(self, event: str) -> bool:
        return event == "TASK_DONE"

# Servicio
class NotificationService:
    def __init__(self, policy: NotificationPolicy):
        self.policy = policy

    def notify(self, event: str):
        if self.policy.should_notify(event):
            print(f"Enviando notificación para el evento: {event}")