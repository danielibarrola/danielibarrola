#include <string>
#include <vector>
#include <set>

class SoftwareEngineer {
public:
    std::string name;
    std::string location;

    SoftwareEngineer(const std::string& name, const std::string& location)
        : name(name), location(location) {}
};

class Experience {
public:
    std::string company;
    std::string position;
    std::string responsibilities;

    Experience(const std::string& company, const std::string& position,
               const std::string& responsibilities)
        : company(company), position(position), responsibilities(responsibilities) {}
};

class Daniel : public SoftwareEngineer {
public:
    Daniel() : SoftwareEngineer("Daniel Ibarrola", "CDMX, Mexico") {}

    std::string describe() const {
        return "I'm " + name + ", a senior engineer who designs and builds cloud-native systems "
               "using Python, AWS, and modern DevOps practices. I specialize in backend architecture, "
               "infrastructure as code, and scalable full-stack applications.";
    }

    std::set<std::string> stack() const {
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
        };
    }

    static std::vector<Experience> experience() {
        return {
            Experience(
                "Grid Dynamics",
                "Senior Software Engineer",
                "Developed ML infrastructure for Google's JAX library, optimized build systems using Bazel, "
                "and created tools in Python. Worked on CI/CD pipelines with GitHub Actions."
            ),
            Experience(
                "Inter-Con Security Systems",
                "Backend Developer",
                "Designing cloud-native architectures with AWS and Terraform, "
                "developing full-stack applications in Python and React, and mentoring junior developers."
            ),
            Experience(
                "Centro de Instrumentación y Registro Sísmico",
                "Software Engineer",
                "Built real-time seismic data systems and automated AWS infrastructure with Terraform."
            ),
            Experience(
                "Hospital Infantil de México Federico Gómez",
                "Software Engineer",
                "Led the development of an open-source pharmacophore modeling library for drug discovery."
            ),
        };
    }
};
