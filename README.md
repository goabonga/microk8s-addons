# 🧩 My MicroK8s Addons Project 🚀

[![MicroK8s](https://img.shields.io/badge/MicroK8s-3C8DBC?style=for-the-badge&logo=kubernetes&logoColor=white)](#)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-blue?style=for-the-badge&logo=kubernetes&logoColor=white)](#)
[![Helm](https://img.shields.io/badge/Helm-blue?style=for-the-badge&logo=helm&logoColor=white)](#)
[![Addons](https://img.shields.io/badge/Addons-Custom-green?style=for-the-badge)](#)
[![Tests](https://img.shields.io/github/actions/workflow/status/goabonga/microk8s-addons/run-tests.yml?style=for-the-badge)](#)

Welcome to **My MicroK8s Addons Project**! This repository is a collection of custom addons for **MicroK8s**, designed to enhance and extend your Kubernetes cluster with modular, reusable components. 

## 🚠 Tech Stack

- **MicroK8s** 🐛 - A lightweight Kubernetes distribution perfect for running on edge devices, IoT, and low-resource environments.
- **Custom Addons** 🧩 - Extend your Kubernetes capabilities with tailored modules.
- **Helm** 🪛 - For packaging and deploying reusable Kubernetes applications.

## 🎯 Features

- **📦 Modular Components** - Use only the addons you need, tailored to your cluster’s needs.
- **🚀 Easy Deployment** - Simple commands to deploy new features in your MicroK8s environment.

## 📦 Installation

Clone the repository and set up your MicroK8s environment:

```bash
git clone https://github.com/goabonga/microk8s-addons.git
cd microk8s-addons
```

Ensure MicroK8s is installed and running on your system.

## 🚀 Getting Started

1. **Enable Addons:** Use `microk8s enable <addon>` to activate specific addons from the collection.
2. **Manage Addons:** Easily update or remove addons with `microk8s disable <addon>`.
3. **Extend Functionality:** Add your own custom addons to the collection to fit your specific use cases.

## 💁️‍💻 Project Structure

```plaintext
microk8s-addons/
│
├── addons/                # Custom addon definitions
│   ├── addon1/            # Addon-specific files (charts, configs, etc.)
│   ├── addon2/            # Addon-specific files (charts, configs, etc.)
│   └── ...
├── addons.yaml            # Main configuration file for all addons
├── CHANGELOG.md           # Changelog of the project
├── CONTRIBUTING.md        # Contribution guidelines
├── description            # Description file for the project
├── HACKING.md             # Guide for developers on modifying and extending the project
├── LICENSE                # License information
├── poetry.lock            # Poetry lock file for dependencies
├── poetry.toml            # Poetry configuration file
├── pyproject.toml         # Project metadata and dependencies
├── README.md              # This file
└── tests/                 # Test suite for the addons
    ├── test_addons.py     # Unit tests for addons
    └── utils.py           # Utility functions for tests
```

## 🤖 Development

To create or modify addons, follow the guidelines outlined in the [contribution guide](CONTRIBUTING.md). Test your addons locally before merging to ensure compatibility.

## 📝 License

This project is licensed under the Proprietary License - see the [LICENSE](LICENSE) file for details.

## 🛧️ Contact

Have questions? Feel free to reach out via [GitHub Issues](https://github.com/goabonga/microk8s-addons/issues).

## 📦 Donate

If you find this project helpful, please consider supporting it! Your contributions will help maintain and improve the project. 

[💖 Donate!](https://github.com/sponsors/goabonga)


---

🌟 If you like this project, give it a star on [GitHub](https://github.com/goabonga/microk8s-addons)! 🌟
