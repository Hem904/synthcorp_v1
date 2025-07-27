| Object         | Description |
|----------------|-------------|
| `MachineFactory` | Factory Pattern class responsible for creating machine command instances. |
| `Command`      | Interface-like object to encapsulate actions. Used in a Command Pattern style. |
| `Invoker`      | Executes commands, decouples action initiator from execution logic. |
| `SynthApp`     | GUI class that handles user interface components. |
| `Main`         | Entrypoint that glues factory, commands, and GUI components. |
| `app.py`       | Support module, may contain orchestration or system-specific logic. |


| Context        | Description |
|----------------|-------------|
| Factory Pattern | Used to instantiate appropriate machine logic classes dynamically based on input or mode. |
| Command Pattern | Enables decoupling of command creation and execution. Makes the system extensible. |
| GUI Handling    | The graphical user interface interacts with users to gather input and invoke backend logic. |
| CLI Support     | Supports command-line interaction through `Main.py` for testing and direct invocation. |



| Context        | Relevant Information |
|----------------|----------------------|
| Factory Pattern | Each machine class must implement a known interface or contract. |
| Command Pattern | `execute()` methods are used to run encapsulated logic. |
| GUI Handling    | Tkinter-based layout with buttons mapped to commands or factory outputs. |
| CLI Support     | Uses `argparse` or manual argument parsing to trigger logic for test or automation. |

