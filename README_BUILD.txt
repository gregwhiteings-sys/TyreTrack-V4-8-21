TYRETRACK V4.8.2 — WINDOWS 11 PORTABLE BUILD

CONTENTS: App source, count_line.py, tyre_detector.pt, PyInstaller spec,
Windows GitHub Actions workflow, and smoke tests.

RECOMMENDED: Use GitHub Actions (Windows runner), not Linux Colab PyInstaller.
1. Create a PRIVATE GitHub repository (the detector model is included).
2. Upload the files/folders in this ZIP, preserving .github/workflows/build-windows.yml.
3. Open Actions > Build TyreTrack Windows > Run workflow.
4. After the run succeeds, download the TyreTrack-Windows-Portable artifact.
5. Extract on Windows 11 and run TyreTrack.exe inside its folder.

The workflow uses CPU-only PyTorch and a portable one-folder build.
The smoke test checks Python imports, detector inference and GUI initialization.
The workflow also launches the packaged executable on Windows in a smoke test.
This DOES NOT verify OAK-D hardware, real conveyor counting, email delivery,
or compatibility with every Windows PC. Test those on the Australian PC.

If the runner fails, open the failed step logs. Never delete needed DLLs to
hide an import error. Package the matching runtime instead.

The model's capabilities control whether Segmentation Mask mode works.
A detection-only model cannot generate genuine segmentation masks.

Email credentials are NOT included. Configure them on the target PC.
