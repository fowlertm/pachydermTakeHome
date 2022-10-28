# Movie, framed: converting films to frames with OpenCV and Pachyderm.

We walk through the process of creating a simple tool which takes `.MOV` files and converts them into frames. The core script is found in `frames.py`, and it relies upon the `opencv` library to slice the movie file into individual frames, which are saved off locally. At the moment we only support the `.MOV` extension, but the script can handle arbitrarily many input files. All data versioning, pipelining, and distributed processing are handled by Pachyderm. Pachyderm is a truly *mammoth* ( :D! ) tool for creating data-centric pipelines, with an immutible data lineage, automated version control, an automated parallel processing.
