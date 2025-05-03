# 🧰 Pydantic-Basic

Welcome to **Pydantic-Basic**, a curated collection of examples demonstrating the capabilities of [Pydantic](https://docs.pydantic.dev/latest/) for data validation and modeling in Python. This repository is designed to help developers understand and utilize Pydantic's features effectively, from foundational concepts to integration with FastAPI.

---

## 📂 Repository Structure

```

Pydantic-Basic/
├── 01\_foundation/
├── 02\_fields/
├── 03\_model\_behaviour/
├── 04\_nested\_model/
├── 05\_serialization/
├── fastapi/
├── main.py
├── README.md
├── LICENSE
├── pyproject.toml
└── uv.lock

````

- **01_foundation/**: Introduction to basic Pydantic models and type annotations.
- **02_fields/**: Exploration of field types, default values, and field constraints.
- **03_model_behaviour/**: Understanding model behaviors, including validators and computed fields.
- **04_nested_model/**: Working with nested and recursive models.
- **05_serialization/**: Demonstrating serialization and custom JSON encoding.
- **fastapi/**: Integrating Pydantic models with FastAPI for building APIs.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.9 or higher installed. You can check your Python version using:

```bash
python --version
````

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sourabh-Kumar04/Pydantic-Basic.git
   cd Pydantic-Basic
   ```

2. **Install `uv`:**

   If you haven't installed `uv` yet, you can do so using pip:

   ```bash
   pip install uv
   ```

3. **Install project dependencies:**

   ```bash
   uv sync
   ```

   This command will install all the dependencies specified in `pyproject.toml` and lock them in `uv.lock`.

---

## 🧪 Usage

Each directory contains Python scripts that can be run independently to observe Pydantic's features in action.

For example, to run the foundational examples:

```bash
uv run 01_foundation/example.py
```

To start the FastAPI application:

```bash
uv run fastapi/fastapi_examples.py
```

---

## 📖 Examples Overview

### ✅ 01\_foundation

* Basic model creation using `BaseModel`.
* Type enforcement and automatic data parsing.

### 🛠️ 02\_fields

* Field definitions with default values.
* Field constraints and aliases.

### 🔄 03\_model\_behaviour

* Custom validators using `@validator`.
* Computed fields with `@property`.

### 🧩 04\_nested\_model

* Nested models to represent complex data structures.
* Recursive models for hierarchical data like comments.

### 📤 05\_serialization

* Model serialization to dictionaries and JSON.
* Custom JSON encoders for complex types like `datetime`.

### 🌐 fastapi

* Building API endpoints with FastAPI.
* Request and response models using Pydantic.

---

## 📘 License

This project is licensed under the [Apache-2.0 License](LICENSE).

---

## 🙋‍♂️ Author

**Sourabh Kumar**

* 💼 [LinkedIn](https://linkedin.com/in/sourabh-kumar04)
* 📧 [Email](mailto:sourabh404sourabh@gmail.com)

Feel free to reach out for collaborations or queries related to this project.

---

## ⭐ Acknowledgments

* [Pydantic Documentation](https://docs.pydantic.dev/latest/)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [uv Documentation](https://docs.astral.sh/uv/)

---

```
This `README.md` reflects the use of `uv` for dependency management and running the FastAPI application. If you need assistance with setting up `pyproject.toml` or have further questions, feel free to ask! 
```
