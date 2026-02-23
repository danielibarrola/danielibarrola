class SoftwareEngineer {
    name: string;
    location: string;

    constructor(name: string, location: string) {
        this.name = name;
        this.location = location;
    }
}

class Experience {
    company: string;
    position: string;
    responsibilities: string;

    constructor(company: string, position: string, responsibilities: string) {
        this.company = company;
        this.position = position;
        this.responsibilities = responsibilities;
    }
}

class Daniel extends SoftwareEngineer {
    constructor() {
        super("Daniel Ibarrola", "CDMX, Mexico");
    }

    describe(): string {
        return `I'm ${this.name}, a senior engineer who designs and builds cloud-native systems ` +
            "using Python, AWS, and modern DevOps practices. I specialize in backend architecture, " +
            "infrastructure as code, and scalable full-stack applications.";
    }

    get stack(): Set<string> {
        return new Set([
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
        ]);
    }

    static experience(): Experience[] {
        return [
            new Experience(
                "Grid Dynamics",
                "Senior Software Engineer",
                "Developed ML infrastructure for Google's JAX library, optimized build systems using Bazel, " +
                "and created tools in Python. Worked on CI/CD pipelines with GitHub Actions."
            ),
            new Experience(
                "Inter-Con Security Systems",
                "Backend Developer",
                "Designing cloud-native architectures with AWS and Terraform, " +
                "developing full-stack applications in Python and React, and mentoring junior developers."
            ),
            new Experience(
                "Centro de Instrumentación y Registro Sísmico",
                "Software Engineer",
                "Built real-time seismic data systems and automated AWS infrastructure with Terraform."
            ),
            new Experience(
                "Hospital Infantil de México Federico Gómez",
                "Software Engineer",
                "Led the development of an open-source pharmacophore modeling library for drug discovery."
            ),
        ];
    }
}
