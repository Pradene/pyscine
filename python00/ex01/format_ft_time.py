import time
from datetime import datetime

epoch = datetime.fromtimestamp(0).strftime("%B %d, %Y")
elapsed = time.time()
date = datetime.now().strftime("%B %d %Y")

print(
    f"Seconds since {epoch}: {elapsed:,.4f} or "
    f"{elapsed:.2e} in scientific notation\n"
    f"{date}"
)
