import os

# Where the code-server tar and plugins are downloaded to
EXECUTABLE_NAME = "code-server"
DOWNLOAD_DIR = "/tmp/code-server"
HOURS_TO_SECONDS = 60 * 60
DEFAULT_UP_SECONDS = 10 * HOURS_TO_SECONDS  # 10 hours
DEFAULT_CODE_SERVER_REMOTE_PATH = (
    "https://github.com/coder/code-server/releases/download/v4.18.0/code-server-4.18.0-linux-amd64.tar.gz"
)
DEFAULT_CODE_SERVER_EXTENSIONS = [
    "https://open-vsx.org/api/ms-python/python/2023.20.0/file/ms-python.python-2023.20.0.vsix",
    "https://open-vsx.org/api/ms-toolsai/jupyter/2023.9.100/file/ms-toolsai.jupyter-2023.9.100.vsix",
]
DEFAULT_CODE_SERVER_DIR_NAME = "code-server-4.18.0-linux-amd64"
# Default max idle seconds to terminate the vscode server
HOURS_TO_SECONDS = 60 * 60
MAX_IDLE_SECONDS = 10 * HOURS_TO_SECONDS  # 10 hours

# Duration to pause the checking of the heartbeat file until the next one
HEARTBEAT_CHECK_SECONDS = 60

# The path is hardcoded by code-server
# https://coder.com/docs/code-server/latest/FAQ#what-is-the-heartbeat-file
HEARTBEAT_PATH = os.path.expanduser("~/.local/share/code-server/heartbeat")
