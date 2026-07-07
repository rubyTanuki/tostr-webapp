from rich.console import Console
from rich.text import Text

console = Console()

# Build your perfectly colored output string
output = Text()

# Header
output.append("\n")
output.append("C-a1b2c3d4e5", style="sky_blue2")
output.append(" | src/auth.py#Authenticator\n")
output.append("[dist: 0.934]\n", style="light_green")
# description
output.append("// Handles the core authentication lifecycle, validating\n   user credentials against the database registry and\n   issuing JWT session tokens for API access.\n", style="italic bright_black")

output.append("C-b4e08bd44f", style="sky_blue2")
output.append(" | src/core/providers.py#AuthProvider\n")
output.append("[dist: 0.915]\n", style="light_green")
# description
output.append("// Abstract base class defining the standard contract for\n   external identity providers (e.g., OAuth2, SAML) to\n   normalize third-party login flows.\n", style="italic bright_black")

output.append("C-c859d3007d", style="sky_blue2")
output.append(" | src/auth/tokens.py#TokenManager\n")
output.append("[dist: 0.882]\n", style="light_green")
# description
output.append("// Manages the cryptographic signing, verification, and\n   automated rotation of access and refresh tokens,\n   ensuring secure stateless session management.\n", style="italic bright_black")

console.print(output)