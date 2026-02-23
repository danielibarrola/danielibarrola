class SoftwareEngineer:

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location


class Experience:
    def __init__(self, company: str, position: str, responsibilities: str):
        self.company = company
        self.position = position
        self.responsibilities = responsibilities


class Daniel(SoftwareEngineer):

    def __init__(self):
        super().__init__(
            name="Daniel Ibarrola", location="CDMX, Mexico"
        )

    def describe(self) -> str:
        return (
            f"I'm {self.name}, a senior engineer who designs and builds cloud-native systems "
            "using Python, AWS, and modern DevOps practices. I specialize in backend architecture, "
            "infrastructure as code, and scalable full-stack applications."
        )

    @property
    def stack(self) -> set[str]:
        return {
            "Python",
            "TypeScript",
            "React",
            "FastAPI",
            "Terraform",
            "Docker",
            "GitHub Actions",
            "Bitbucket Pipelines",
            "AWS",
            "PostgreSQL",
            "DynamoDB",
            "Bazel",
        }

    @staticmethod
    def experience() -> list[Experience]:
        return [
            Experience(
                company="Grid Dynamics",
                position="Senior Software Engineer",
                responsibilities=(
                    "Developed ML infrastructure for Google’s JAX library, optimized build systems using Bazel, "
                    "and created tools in Python. Worked on CI/CD pipelines with GitHub Actions."
                ),
            ),
            Experience(
                company="Inter-Con Security Systems",
                position="Backend Developer",
                responsibilities=(
                    "Designing cloud-native architectures with AWS and Terraform, "
                    "developing full-stack applications in Python and React, and mentoring junior developers."
                ),
            ),
            Experience(
                company="Centro de Instrumentación y Registro Sísmico",
                position="Software Engineer",
                responsibilities=(
                    "Built real-time seismic data systems and automated AWS infrastructure with Terraform."
                ),
            ),
            Experience(
                company="Hospital Infantil de México Federico Gómez",
                position="Software Engineer",
                responsibilities=(
                    "Led the development of an open-source pharmacophore modeling library for drug discovery."
                ),
            ),
        ]
