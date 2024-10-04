<!--
Hey, thanks for using the awesome-readme-template template.  
If you have any enhancements, then fork this project and create a pull request 
or just open an issue with the label "enhancement".

Don't forget to give this project a star for additional support ;)
Maybe you can mention me or this repo in the acknowledgements too
-->
<div align="center">

  <img src="assets/logo.svg" alt="logo" width="200" height="auto" />
  <h1>BrisviLock</h1>
  
  <p>
    A next-generation encryption lock for USB devices.
  </p>
  
<!-- Badges -->
<p>
  <a href="https://github.com/gabriel7zoo/BrisviLock/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/gabriel7zoo/BrisviLock" alt="contributors" />
  </a>
  <a href="https://github.com/gabriel7zoo/BrisviLock/commits/main">
    <img src="https://img.shields.io/github/last-commit/gabriel7zoo/BrisviLock" alt="last update" />
  </a>
  <a href="https://github.com/gabriel7zoo/BrisviLock/network/members">
    <img src="https://img.shields.io/github/forks/gabriel7zoo/BrisviLock" alt="forks" />
  </a>
  <a href="https://github.com/gabriel7zoo/BrisviLock/stargazers">
    <img src="https://img.shields.io/github/stars/gabriel7zoo/BrisviLock" alt="stars" />
  </a>
  <a href="https://github.com/gabriel7zoo/BrisviLock/issues/">
    <img src="https://img.shields.io/github/issues/gabriel7zoo/BrisviLock" alt="open issues" />
  </a>
  <a href="https://github.com/gabriel7zoo/BrisviLock/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/gabriel7zoo/BrisviLock.svg" alt="license" />
  </a>
</p>

<h4>
    <a href="https://github.com/gabriel7zoo/BrisviLock/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/gabriel7zoo/BrisviLock">Documentation</a>
  <span> · </span>
    <a href="https://github.com/gabriel7zoo/BrisviLock/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/gabriel7zoo/BrisviLock/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
  * [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
  * [Running Tests](#test_tube-running-tests)
  * [Run Locally](#running-run-locally)
  * [Deployment](#triangular_flag_on_post-deployment)
- [Usage](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
  * [Code of Conduct](#scroll-code-of-conduct)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

<!-- About the Project -->
## :star2: About the Project

**BrisviLock** is an advanced encryption tool that allows you to securely store files on USB devices. Files uploaded using the **BrisviLock** script will remain hidden from view unless accessed through the application, ensuring your data remains confidential.

### :camera: Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>

### :space_invader: Tech Stack

- **Languages**: Python
- **Frameworks**: [Flask](https://flask.palletsprojects.com/)
- **Libraries**: [Cryptography](https://cryptography.io/en/latest/)

### :dart: Features

- **File Encryption**: Secure your files using strong encryption algorithms.
- **File Hiding**: Uploaded files won't be visible on the USB drive unless accessed through **BrisviLock**.
- **Cross-Platform**: Runs on any platform with Python installed.
- **User-Friendly CLI**: Simple command-line interface for ease of use.

### :key: Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

```
getpassword=1235
```

<!-- Getting Started -->
## :toolbox: Getting Started

### :bangbang: Prerequisites

- Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### :gear: Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gabriel7zoo/BrisviLock.git
   cd BrisviLock
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a directory for hidden files:

   ```bash
   mkdir hidden_files
   ```

### :test_tube: Running Tests

To run tests, execute the following command:

```bash
pytest
```

### :running: Run Locally

1. Clone the project:

   ```bash
   git clone https://github.com/gabriel7zoo/BrisviLock.git
   ```

2. Go to the project directory:

   ```bash
   cd BrisviLock
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python brisvi.py
   ```

### :triangular_flag_on_post: Deployment

To deploy this project, follow your preferred method for deploying Python applications, such as using Docker or a cloud platform.

<!-- Usage -->
## :eyes: Usage

Use this section to provide additional information on how to use **BrisviLock**, including code samples or links to further documentation.

```bash
python brisvi.py
```

Follow the prompts to encrypt or decrypt your files.

<!-- Roadmap -->
## :compass: Roadmap

* [x] Initial release
* [ ] Add more encryption options
* [ ] Implement a graphical user interface

<!-- Contributing -->
## :wave: Contributing

<a href="https://github.com/gabriel7zoo/BrisviLock/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=gabriel7zoo/BrisviLock" />
</a>

Contributions are always welcome! See `CONTRIBUTING.md` for ways to get started.

### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/gabriel7zoo/BrisviLock/blob/main/CODE_OF_CONDUCT.md).

<!-- FAQ -->
## :grey_question: FAQ

- **Question 1**: What platforms does BrisviLock support?
  
  + **Answer**: BrisviLock is cross-platform and can run on any operating system that supports Python.

- **Question 2**: How do I access my encrypted files?
  
  + **Answer**: You need to run the **BrisviLock** script and provide the necessary encryption key to access your files.

<!-- License -->
## :warning: License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- Contact -->
## :handshake: Contact

Gabriel Zoo - [@gabriel7zoo](https://twitter.com/gabriel7zoo) - gabriel7zoo@yahoo.com

Project Link: [https://github.com/gabriel7zoo/BrisviLock](https://github.com/gabriel7zoo/BrisviLock)

<!-- Acknowledgements -->
## :gem: Acknowledgements

- [Shields.io](https://shields.io/)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#travel--places)
- [Readme Template](https://github.com/othneildrew/Best-README-Template)
