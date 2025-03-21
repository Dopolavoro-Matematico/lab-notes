import qrcode

# Replace this with your actual GitHub repo or GitHub Pages URL
repo_url = "https://yourusername.github.io/math-lab-notes/"

# Generate QR code
qr = qrcode.make(repo_url)

# Save to file
qr.save("qr-code.png")

print(f"QR code saved for {repo_url}")
