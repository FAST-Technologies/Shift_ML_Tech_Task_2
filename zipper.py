import zipfile

print("\nСоздание архива submission.zip...")

with zipfile.ZipFile("submission.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("data/submission.csv")
    zipf.write("data/requirements.txt")
    zipf.write("notebooks/competition.ipynb")

print("Архив submission.zip создан успешно!")
print("\nСодержимое архива:")
with zipfile.ZipFile("submission.zip", "r") as zipf:
    for file in zipf.namelist():
        print(f"  - {file}")
