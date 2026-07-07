from rich.console import Console
from rich.text import Text

console = Console()

# Build your perfectly colored output string
output = Text()

# Header
output.append("\n")
output.append("C-a1b2c3d4e5", style="sky_blue2")
output.append(" @L15-220", style="light_green")
output.append(" | src/auth.py#Authenticator\n")
# description
output.append("// Handles the core authentication lifecycle, validating\n   user credentials against the database registry and\n   issuing JWT session tokens for API access.\n", style="italic bright_black")
# dependencies
output.append("< C-b4e08bd44f|src/core/providers.py#AuthProvider\n> C-123456|src/db/base.py#DatabaseClient\n", style="bright_magenta")

# children
output.append("fields:\n", style="bright_yellow")
output.append("     V-8a1c8a0dd5", style="sky_blue2")
output.append(" | _client: DatabaseClient\n")
output.append("     V-c8f93b2a11", style="sky_blue2")
output.append(" | jwt_secret: SecretStr \n")
output.append("     V-d9e04c3b22", style="sky_blue2")
output.append(" | session_timeout_seconds: int\n")

output.append("methods:\n", style="bright_yellow")
output.append("     M-7f701a3e6f", style="sky_blue2")
output.append(" | def __init__(self, db_client:DatabaseClient)\n")
output.append("     // Initializes the authenticator by binding the \n        persistent database connection and loading\n        cryptographic signing configurations. \n", style="italic bright_black")
output.append("     M-e0f15d4c33", style="sky_blue2")
output.append(" | def authenticate_user(self, credentials:\n UserCredentials) -> AuthToken\n")
output.append("     // Cryptographically hashes and validates the ...", style="italic bright_black")

console.print(output)