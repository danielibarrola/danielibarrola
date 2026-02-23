
import argparse
import os


def get_language_from_extension(filename: str) -> str:
    """ Determine the language based on file extension."""
    ext = os.path.splitext(filename)[1]
    extension_map = {
        ".py": "Python",
        ".ts": "TypeScript",
        ".cpp": "C++",
    }
    return extension_map.get(ext, "")


def get_code(filename: str = "me.py") -> list[str]:
    """ Get the code from the specified file starting from the Daniel class.

    Args:
        filename: Name of the file to read (default: me.py)
    """
    language = get_language_from_extension(filename)
    code = [
        f"```{language}\n",
    ]

    add_line = False
    with open(filename, "r") as fp:
        for line in fp.readlines():
            if line.startswith("class Daniel"):
                add_line = True
            if add_line:
                code.append(line)

    code.append("```")
    return code


def main() -> None:
    """ Creates or updates the readme file."""
    parser = argparse.ArgumentParser(
        description="Update README.md with code from a specified file"
    )
    parser.add_argument(
        "filename",
        nargs="?",
        default="me.py",
        help="Name of the file to parse (default: me.py)"
    )

    args = parser.parse_args()

    header = [
        "#  👋 Hi, I'm Daniel\n",
        "[![Linkedin: Daniel-Ibarrola](https://img.shields.io/badge/-DanielIbarrola-blue?style=flat-square&logo"
        "=Linkedin&logoColor=white&link=https://www.linkedin.com/in/d-ibarrola/)]("
        "https://www.linkedin.com/in/d-ibarrola/)\n",
        "[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)]("
        "https://github.com/ellerbrock/open-source-badge/)\n",
    ]

    code = get_code(args.filename)
    with open("../README.md", "w") as fp:
        fp.writelines(header)
        fp.writelines(code)

    print("DONE")


if __name__ == "__main__":
    main()
