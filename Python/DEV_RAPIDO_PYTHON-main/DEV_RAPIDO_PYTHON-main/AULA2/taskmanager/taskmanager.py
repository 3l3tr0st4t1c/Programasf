from task import Task

class TaskManager:
    def __init__(self: object) -> None:
        self.tasks = []

    def adicionar_tarefa(self: object, task: Task) -> None:
        self.tasks.append(task)

    def listar_tarefa(self: object) -> None:
        for task in self.tasks:
            estado = "Concluída" if task.status else "Pendente" 
            print(f"Titulo : {task.titulo}, Descricao : {task.descricao} | Status: {estado}")

    def marcar_concluida(self: object, titulo: str):
        for tks in self.tasks:
            if tks.titulo.lower() == titulo.lower():
                tks.status = True
                print(f"Tarefa {tks.titulo} concluida")

if __name__ == "__main__":
    Task_manager = TaskManager()
    Task_manager.adicionar_tarefa(Task("Fazer Compra", "comprar leite em pó"))
    Task_manager.adicionar_tarefa(Task("Estudar Python", "Resolver Exercicios"))
    Task_manager.listar_tarefa()
    Task_manager.marcar_concluida("Fazer Compra")
    Task_manager.listar_tarefa()