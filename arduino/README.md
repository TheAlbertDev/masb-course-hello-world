# Hello, World!

<img align="left" src="https://img.shields.io/badge/Environment-Arduino-blue"><img align="left" src="https://img.shields.io/badge/Estimated_duration-2 h-green"></br>

When learning a new programming language—or, in this case, programming for a new _target_ (the device you want to control)—it is traditional to begin with a **"Hello, World!"** program. Typically, "Hello, World!" programs are small applications that run on the _host_ (your personal computer, or PC) and display the phrase "Hello, World!" on the screen.

In embedded systems, the _target_ is the microcontroller or device you are programming, while the _host_ is your development computer. Since our microcontroller does not have a screen, the equivalent of "Hello, World!" is to make an LED blink. In this exercise, we will go a step further: we will make the [LED](https://en.wikipedia.org/wiki/Light-emitting_diode) turn on at our command using the button (or _push button_) on the Evaluation Board ([EVB](https://en.wikipedia.org/wiki/Microprocessor_development_board)).

In this exercise, we will learn to create a program using Arduino. We will use one of the fundamental features of microcontrollers: digital GPIOs (General Purpose Input/Output). A GPIO is a pin on the microcontroller that can be configured as either an input or an output. GPIOs are used in countless devices and applications, such as:

- Detecting button presses
- Generating indicators in user interfaces (like turning on LEDs)
- Detecting or generating events in biomedical devices (e.g., detecting the presence of a sensor strip in a glucometer)
- Monitoring the power status of a battery-powered _Point-of-Care_ (PoC) device
- Many other uses

## Objectives

- Become familiar with the STM32 Nucleo-F401RE EVB.
- Learn about the PlatformIO IDE and how it works.
- Create, compile, and upload your first program in Arduino.
- Use GPIOs as both inputs and outputs.
- Gain an introduction to version control systems (VCS), specifically Git.

## Procedure

### IDE Preparation and Digital Outputs

#### IDE Preparation

The first step is to install the application used to develop Arduino-based programs: PlatformIO IDE. IDE stands for [_Integrated Development Environment_](https://en.wikipedia.org/wiki/Integrated_development_environment). An IDE is an application that provides the necessary tools to develop, compile, deploy, and debug software.

##### Step-by-Step: Setting Up Your Development Environment

1. **Install Visual Studio Code (VS Code):**

- Download VS Code from [this link](https://code.visualstudio.com) if it is not already installed on your computer.
- The application is available for multiple operating systems (OS). The exercises can be performed on any OS compatible with the application.

2. **Import the Pre-configured VS Code Profile:**

- Both PlatformIO IDE and STM32Cube, which will be used in the next part of the practice, run on VS Code.
- VS Code allows you to work with different profiles. For example, you can have a profile for Python development with certain modules installed, and another for JavaScript programming with other modules.
- To make setup easier, I have prepared two VS Code profiles that you can import, each pre-configured with all the modules we will need during the course. This way, you can skip the manual configuration and simply import the profiles. When starting an Arduino or STM32Cube exercise, remember to activate the relevant profile.
- You can find the PlatformIO environment profile at the following link: [MASB Arduino](https://vscode.dev/profile/github/8ba47b7a695fa1d654c7b084ae74a78b). This will open a VS Code editor in your browser. Wait for the profile to load (this may take a while), and once it appears, select and import it into your VS Code as shown in the image below. When the profile is activated, the PlatformIO branding colors are set in the activity bar to show that the profile is active.

![](/.github/images/vscode-import-profile.png)

##### Arduino IDE vs. PlatformIO

Normally, when starting with Arduino, the Arduino IDE is used for programming. However, in this course, we will use PlatformIO, which is based on VS Code. PlatformIO is just as easy to install and use, but it allows for more advanced actions, such as creating projects with `.cpp` and `.hpp` files (standard C++ files) instead of only using the `.ino` format (the Arduino file format).

**Key differences:**

- **Arduino IDE:**
  - Uses `.ino` files or _sketches_ and automatically converts them behind the scenes into `.cpp` and `.hpp` files.
  - Hides some aspects of the C/C++ language, which can cause confusion as you progress in your development skills.

- **PlatformIO:**
  - Lets you work directly with standard C++ files (`.cpp`, `.hpp`), giving you more control and a better understanding of how embedded software is structured.
  - Integrates advanced features such as project management, version control, and debugging tools.

Detailed instructions on how to install PlatformIO IDE can be found at this [link](https://docs.platformio.org/en/latest/integration/ide/vscode.html#installation).

![](/.github/images/platformio-extension.png)

#### The STM32 Nucleo-F401RE EVB

As mentioned earlier, the EVB we will use is the STM32 Nucleo-F401RE from STMicroelectronics. This EVB features the [STM32F401RET6U](https://www.st.com/en/product/STM32F401RE) microcontroller from the same manufacturer.

One of the key advantages of EVBs is that they provide a quick and cost-effective way to prototype microcontroller-based devices. For example, the STM32 Nucleo-F401RE has a current retail price of around €15 and already includes an integrated _debugger_ (the electronic circuit required to program the microcontroller). A standalone official debugger can cost over €100.

Manufacturers create these EVBs to facilitate entry into their development ecosystem at a low cost, ultimately encouraging developers to adopt their microcontrollers. Another advantage is that the EVB exposes all the microcontroller's pins, making it easier to connect external components during the prototyping phase and eliminating the need to design custom prototype boards—saving significant costs in design, components, manufacturing, and testing.

Below is an image of the EVB we will use.

![](/.github/images/stm32-nucleo-f401re.png)

The schematic of the EVB can be found [here](https://www.st.com/resource/en/schematic_pack/mb1136-default-c04_schematic.pdf). Three other important documents, which we will not yet use in this Arduino practice, are: the [microcontroller datasheet](https://www.st.com/resource/en/datasheet/stm32f401re.pdf), the [reference manual for the microcontroller family](https://www.st.com/resource/en/reference_manual/dm00096844.pdf), and the [user manual for the HAL (Hardware Abstraction Layer) libraries](https://www.st.com/resource/en/user_manual/dm00105879.pdf).

#### Now, Let's Say: Hello, World!

##### Cloning the Repository

In this and all other course practices, a [version control system (VCS)](https://en.wikipedia.org/wiki/Version_control) is used for development, collaboration, and submission of assignments and projects. The details of how VCS works will be gradually introduced in each practice. For now, I ask for a small leap of faith—just follow the Git instructions carefully. We will explain the commands and terms as they appear.

Since this is the first lab session, if you haven't done so already, we will go through the process of cloning the remote [repository](<https://en.wikipedia.org/wiki/Repository_(version_control)>) from GitHub to your computer. This means having a local copy of all the content stored in GitHub and establishing a link to the remote repository. This link will allow you to retrieve versions and branches hosted on the server and push your changes.

To do this, navigate to the main page of the [repository]({{ github_repo_url }}) and copy the link available in the green **Clone or Download** button. Make sure you copy the link while it says **Clone with HTTPS** and not **Clone with SSH**.

Once the link is copied, go to the folder where you want to store your local repository.

> [!WARNING]
> Choose a folder whose path contains only alphanumeric characters (without accents or special characters), hyphens, or underscores, and does not contain spaces. If anyone contacts me saying "X doesn't work" and I see their course folders are in `Blablabla/One Drive/Enginyeria Biomèdica/Blablabla`, I'll be very annoyed! 👿 (Just kidding, but if you encounter any errors, please check this first.)
>
> Recommended examples: on macOS or Linux, use your home folder; on Windows, you can create a folder like `C:/MASB/Blablabla`.

Right-click on an empty space (not on any file or folder) and select **Git Bash here** from the dropdown menu. If you are on a Windows machine and this option does not appear, it is likely that Git is not installed. You can install it by downloading it from this [link](https://git-scm.com/) and following the steps: Next, Next, Next, ..., and Finish. If you use macOS or Linux, you must access the folder using the terminal. If Git is not installed, follow the proper installation instructions for your OS from the previous link.

> [!NOTE]
> It is important to keep in mind that **Git and GitHub are different things**. Git is the actual VCS and is open source. On the other hand, GitHub is a company that provides a website using Git to store the version history on a remote server, enabling collaboration and sharing (among many other features that we will gradually explore).

When clicking on **Git Bash here**, a Bash terminal will open. There, execute the following command:

```bash
git clone {{ github_repo_git_url }}
```

If not now, then at some point, Git will ask for your credentials. You must enter your GitHub username and a Personal Access Token (PAT) as the password. You can find instructions on how to create a PAT [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic). Create a classic-type PAT and make sure to enable all scopes and permissions, and set no expiration to ensure proper access. Then, you can use the PAT as your password when prompted for credentials by Git in the terminal, as indicated [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#using-a-personal-access-token-on-the-command-line).

With all of this, the remote repository on GitHub has been cloned to your computer, and you can start working.

> [!IMPORTANT]
> When cloning or initializing a repository, a `.git` folder is created, which is typically hidden. **Do not delete this folder**, or the version control in your local repository will be lost, and you will not be able to push your work.
>
> You will also find a folder named `.github` and a file named `.gitignore`. Do not delete these either. The first contains the automation files for the exercise, while the second defines files that should not be added to version control.

One last step is to enter your name and email in the Git configuration so that they appear when you make commits to your local repository. The name and email can be set for just the current repository or globally for all repositories. We will do the latter:

```bash
git config --global user.name "{{ github_student_name }}"
git config --global user.email "{{ github_student_email }}"
```

> [!NOTE]
> I've attempted to automate the generation of these custom commands with your specific GitHub username and email. However, if your email address is set to private in your GitHub account settings, the automated script cannot access it programmatically. In such cases, you'll need to input in the command above the actual email address configured in your GitHub account. You can find your email settings in GitHub by going to Settings → Emails.

If you remove the `--global` from the command, you will be setting the name and email only for the current repository. (Therefore, do not use `--global` if you are on a shared computer with different repositories.)

Here comes the first leap of faith. Enter the local repository folder:

```bash
cd {{ github_repo_name }}
```

And run the following command:

```bash
git switch -c {{ digital_outputs_branch_name }}
```

With this command, you create a branch named `{{ digital_outputs_branch_name }}` and switch to it. A branch is a separate line of development in the repository where you can work in parallel without interfering with the main development or with other team members. By the end of the practice, there will be more than one branch. From here on, do not close the terminal as we will use it to make various commits. (If you close the terminal: no problem. Just open it again as before from within the `{{ github_repo_name }}` folder.)

> [!NOTE]
> The `branch` suffix in the branch name is superfluous and is not usually included. It has been added in this first practice to avoid confusion by preventing branches, folders, and projects from having the same name.

##### Create a Project

Great. We now have our local repository on our computer. Now let's create the project where we will develop our program with PlatformIO. To create a project, simply open VS Code, click on the PlatformIO icon in the sidebar (the icon that looks like an alien/insect head), and then click on "Create New Project." A tab called "PIO Home" will open. There, click on "+ New Project."

![](/.github/images/platformio-project-creation.png)

In the form that appears, enter `{{ digital_outputs_project_name }}` as the project name, select `ST Nucleo F401RE` as the board, and choose `Arduino` as the framework. Finally, uncheck the option to create the project in the default location. Choose to save it in a `{{ platformio_folder_name }}` folder that you will create inside your local repository (the folder you just cloned). Click "Finish" and wait for the project to initialize.

![](/.github/images/platformio-project-wizard.png)

> [!WARNING]
> It is **very important** that you save all files in the specified paths or directories using the indicated path and name. Automated tests will be executed remotely at some checkpoints (Pull Requests), so if the files are not placed in the correct path, tests will fail.

Once the project is created in a folder named as the project (`{{ digital_outputs_project_name }}`) in the selected `{{ platformio_folder_name }}` folder, PlatformIO will automatically add it to your VS Code workspace, ready for you to start working.

Let's open the file `src/main.cpp`.

![](/.github/images/platformio-main.png)

You will find the following:

```c++
#include <Arduino.h>

// put function declarations here:
int myFunction(int, int);

void setup()
{
  // put your setup code here, to run once:
  int result = myFunction(2, 3);
}

void loop()
{
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y)
{
  return x + y;
}
```

The code shown is the default main file generated by PlatformIO for Arduino-based projects. It includes the Arduino library with `#include <Arduino.h>`, and provides empty `setup()` and `loop()` functions, which are required entry points for Arduino programs. The `setup` function is executed once at the beginning of the program and is usually used to initialize variables, peripherals, etc. On the other hand, the `loop` function, once `setup` has been executed, will run continuously. This is where the desired behavior for the microcontroller is coded.

Unlike the Arduino IDE, which uses `.ino` files or _sketches_ and automatically handles some C++ details behind the scenes (such as including `Arduino.h` and managing [function prototypes](https://www.geeksforgeeks.org/c/function-prototype-in-c/)), PlatformIO uses standard C++ `.cpp` files. This means you must explicitly include `Arduino.h` and declare function prototypes, as shown with `int myFunction(int, int);`. This approach exposes you to the full C++ language, making your code more portable and suitable for professional development and automated testing.

Let's start by cleaning up the default code in `src/main.cpp`. **Delete** the `myFunction` declaration at the top of the file, **delete** the `myFunction` definition at the bottom of the file, and **empty** the `setup` and `loop` functions so the file `main.cpp` looks like this:

```cpp
#include <Arduino.h>

void setup()
{
  // put your setup code here, to run once:
}

void loop()
{
  // put your main code here, to run repeatedly:
}
```

This ensures that your file is ready for you to begin writing your own code from scratch. We are going to create a program that makes the EVB's LED blink every 1 second.

##### Digital Outputs: Blink the LED

The LED is connected to pin D13 of the Arduino connector. The `D` denotes that this pin is a digital GPIO that we will use as an output. GPIO stands for _General Purpose Input/Output_ and is a pin on the microcontroller that can perform various functions (e.g., capturing an analog signal, generating a PWM, programming the microcontroller, etc.), both as input (reading) and output (generating a signal). In this case, we will send a digital signal to the LED to turn it on and off. When the digital output signal is `0`, the LED will be off. When it's `1`, the LED will be on.

> [!NOTE]
> It's important to note that in the digital world, we work with a binary system, meaning ones and zeros. But this is at a logical level. At a physical level, these binary values of `0` and `1` are translated to defined voltage levels. These voltage levels are usually 0 V for a `0` and the supply voltage of the microcontroller for a `1`. In this case, the EVB powers the microcontroller with 3.3 V, so a binary `1` corresponds to a voltage level of 3.3 V.

So, the first thing we need to do is configure pin D13 as a digital output GPIO. Since the function of the pin will not change throughout the program, we only need to configure it once. Therefore, the configuration will be done using the `pinMode` instruction within the `setup` function.

```c++
#include <Arduino.h>

void setup()
{
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);   // we configure pin 13 as a digital output pin.
  digitalWrite(13, LOW); // we configure the LED to be off when the program starts.
}

void loop()
{
  // put your main code here, to run repeatedly:
}
```

In the `pinMode` function, we configured pin 13 as an `OUTPUT` or output pin. If we wanted to set it as input (reading a digital value), we would specify `INPUT`. We also added a second instruction, `digitalWrite`, which tells the microcontroller what value to output through the specified pin. If we indicate `LOW`, we are telling it to output a `0`. If we specify `HIGH`, we are telling it to output a `1`.

> [!IMPORTANT]
> A note for navigators: It is very tempting to copy and paste the code from the document instead of writing it yourself. I warn you in advance that this would be a serious mistake. Not because you can't do it (you can), but because you will not understand or integrate the concepts being studied in the lab sessions, and it will be very difficult for you to tackle the final project on your own.

Now, what we are going to do is make the LED blink. This will happen continuously during the execution of the program, so we will code it in the `loop` function. We have just seen the `digitalWrite` function to set an output value. To make the LED blink, we only need to use this function, alternating between `LOW` and `HIGH`.

```c++
#include <Arduino.h>

void setup()
{
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);   // we configure pin 13 as a digital output pin.
  digitalWrite(13, LOW); // we configure the LED to be off when the program starts.
}

void loop()
{
  // put your main code here, to run repeatedly:
  digitalWrite(13, HIGH); // LED on
  digitalWrite(13, LOW);  // LED off
}
```

We build the program and, if everything is correct, the PlatformIO IDE terminal should not show any errors but should display additional information, such as the space the program occupies within the microcontroller's memory, the maximum space it could occupy, etc.

![](/.github/images/platformio-build.png)

Connect the EVB to the computer using the USB cable if you haven't already, and upload the program.

![](/.github/images/platformio-upload.png)

> [!NOTE]
> PlatformIO IDE automatically selects the device. If you have more than one device connected, you can choose which device to upload the project to through the project's `platformio.ini` configuration file. You can find more information [here](https://docs.platformio.org/en/stable/projectconf/sections/env/options/upload/upload_port.html).

Once uploaded... is the LED blinking?

At first glance, it seems like the LED isn't blinking. In reality, it is, but at such a speed that our eyes can't perceive it. Let's tell the microcontroller to wait 1 second between turning the LED on and off. For this, we will use the `delay` function provided by Arduino. This function takes the number of milliseconds you want the microcontroller to wait as its argument. While the microcontroller is waiting within the `delay` function, it doesn't do anything else. Here's how the code looks after adding the delay:

```c++
#include <Arduino.h>

void setup()
{
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);   // we configure pin 13 as a digital output pin.
  digitalWrite(13, LOW); // we configure the LED to be off when the program starts.
}

void loop()
{
  // put your main code here, to run repeatedly:
  // Turn the LED on
  digitalWrite(13, HIGH);
  // Wait for 1 second (1000 milliseconds)
  delay(1000);
  // Turn the LED off
  digitalWrite(13, LOW);
  // Wait for 1 second (1000 milliseconds)
  delay(1000);
}
```

Now, build and upload the program, and you will see how the LED blinks every 1 second.

##### Commit the Version

We have a working program. Let's save this version to ensure that you can always revert to this version of the code if you change something you shouldn't. Run the following command:

```bash
git add {{ platformio_folder_name}}/{{ digital_outputs_project_name }}/
```

With this command, you add the `{{ platformio_folder_name}}/{{ digital_outputs_project_name }}` folder to the stage. The stage is simply an area where you place the files whose version you want to save. Once the files you want to save are added to the stage, you will make the commit. And that's what we're going to do now:

```bash
git commit -m "make LED blink every 1 second"
```

The command is simple and you just need to add a descriptive message of the changes made since the last commit. You've just saved your first version of the code!

#### Pull Request

A **Pull Request (PR)** is a feature in GitHub that allows you to propose changes from one branch (e.g., `{{ digital_outputs_branch_name }}`) into another branch (e.g., `main`). It enables code review, automated testing, and collaboration before merging your work into the main project.

##### How to Create a Pull Request

1. Push your changes to the remote repository using the following command:

```bash
git push
```

This command uploads the changes from the local repository to the remote repository on GitHub. This way, you can share the changes made with the rest of the team. If a branch is created in the local repository that doesn’t yet exist in the remote repository, when doing a push, Git will notify you and ask you to use a special command. Copy and paste the command that Git provides you when doing the push and run it in the terminal:

```bash
 git push --set-upstream origin {{ digital_outputs_branch_name }}
```

2. Go to the GitHub web interface for your [repository]({{ github_repo_url }}).
3. Click the **Pull request** tab and then **New pull request**.
4. Ensure the base branch is `main` and the compare branch is `{{ digital_outputs_branch_name }}`.
5. Add a descriptive title and comment, then click **Create pull request**.

##### Automated Tests

When you create or update a Pull Request (by pushing new commits to the `{{ digital_outputs_branch_name }}` branch), automated tests will be triggered. These tests have been specifically implemented and configured for this course and are executed remotely on a Raspberry Pi (RPi) that is powered on 24/7 and has the same EVB (STM32 Nucleo-F401RE) connected to it. The RPi loads your program into the connected EVB and checks that the defined requirements for the lesson are accomplished (in this case, blinking the LED every 1 second). The status and results of the tests are shown directly in the Pull Request.

> [!NOTE]
> There is only one Raspberry Pi available for testing, and it cannot run multiple tests simultaneously. If another student is running a test, you must wait for their test to finish before yours can start.
>
> If your test remains in the "queued" state for a long time (more than 1 hour), please post your issue in the [GitHub discussion forum](https://github.com/TheAlbertDev/MASB/discussions). This could mean the RPi has lost power supply or network connection.

###### How to Check Test Results

After the tests run, you will see their status in the **Checks** tab of the Pull Request page:

- If all tests pass, you will see a green checkmark.
- If any test fails, you will see a red cross and details about the failure.

TODO: actualizar imagen sin mensaje del bot
![](/.github/images/pull-request-results.png)

If a test fails, please refer to the logs provided in the Pull Request to find the problem or reason for the failure and try to solve it. If you are unable to find or fix the issue, please post your issue in the [GitHub discussion forum](https://github.com/TheAlbertDev/MASB/discussions) for support.

To make any necessary corrections, simply modify the code to fix the bugs, add the changes to Git, and push them. The Pull Request will detect that there are new commits and will re-run the tests.

##### Merging the Pull Request

**Once all tests have passed**, you can merge your developments into the `main` branch by clicking the **Merge pull request** button.

> [!NOTE]
> Normally, merged branches should be deleted to keep the repository clean. However, for academic purposes, we will keep them alive.

### Digital Inputs

We know how to output zeros and ones through the GPIOs. Now let's see how to read them. To do this, we will use the B1 button on the EVB. From this button, as we can see in the schematic of the EVB, it outputs a `1` when not pressed and a `0` when pressed. This behavior is commonly described as _active-low_ because it indicates an action (in this case, pressing a button) by generating a `0`. If it were the opposite, it would be (oh, surprise) _active-high_.

The output from button B1 is connected to pin 23. This pin is not found by default on the original Arduino UNO boards since they do not provide a button. Therefore, if you look in the Arduino connector, you won't find anything. Let's configure it as a digital GPIO input so that the LED toggles between off and on when we press button B1. To configure a pin as input, we use the same `pinMode` function that we used with the LED, but this time specifying `INPUT`.

> [!NOTE]
> There's a third option available for `pinMode`, which is `INPUT_PULLUP`. With this third option, in addition to configuring the pin as input, we indicate that the microcontroller's [pull-up resistor](https://en.wikipedia.org/wiki/Pull-up_resistor) should be enabled.

#### Synchronizing the main branch and creating the project

First, let's switch back to the main branch:

```bash
git switch main
```

On the main branch, we have merged the developments from the previous section that were in the `{{ digital_outputs_branch_name }}` branch. This merge was done from the web, so the changes are not yet reflected in our local repository. To incorporate the changes from the remote repository, run the following command:

```bash
git pull
```

Now our main branch matches the remote repository. Next, as in the previous issue, let's create a new branch for this development. We'll call it `{{ digital_inputs_branch_name }}`:

```bash
git switch -c {{ digital_inputs_branch_name }}
```

Once we're in the correct branch, let's create a project named `{{ digital_inputs_project_name }}` in the folder `{{ platformio_folder_name }}`. You already know how to do this from the previous section.

#### Read the button to change the state of the LED

To toggle between states, we will use the `digitalRead` function to read the pin's input value and use an `if` statement to establish the desired logic. We can also use the `digitalRead` function to check the current state of the LED. This would be the code:

```c++
#include <Arduino.h>

void setup()
{
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);   // configure pin 13 as a digital output pin
  digitalWrite(13, LOW); // configure the LED to be off at the start of the program
  pinMode(23, INPUT);    // configure pin 23 as a digital input pin without pullup
}

void loop()
{
  // put your main code here, to run repeatedly:
  if (digitalRead(23) == LOW)
  { // if the button is pressed
    if (digitalRead(13) == HIGH)
    {                        // if the LED is on
      digitalWrite(13, LOW); // turn it off
    }
    else
    {                         // if it's not on
      digitalWrite(13, HIGH); // turn it on
    }
  }
}
```

We build and upload the program. We press the button and... does it work? Press it a few more times... seems like it does, but sometimes it doesn't..., now and then..., ... , something's wrong...

Once again, our eyes and our _speed_ limit us in front of the microcontroller. The program we’ve written really works. So, what's the problem? The microcontroller is so fast that during a single press, the `loop` function has been executed many times, and the LED blinks rapidly without us perceiving it, leaving the last iteration of the `loop` function randomly turning the LED on or off. This needs to be fixed. How? By making the microcontroller control the LED based on the transition from `0` to `1` or from `1` to `0`, not based on the input value of `0` or `1`. Even though the microcontroller is very fast, a transition will only happen every time we press or release the button, regardless of the press duration. Transition activation is known as _edge triggered_, while level activation is known as _level triggered_.

> [!NOTE]
> The clock system of a microcontroller controls its instruction execution. The clock system generates a square wave signal. The microcontroller executes an instruction every time a transition from `0` to `1` occurs. That is, a microcontroller operates internally in _edge triggered_ mode.

To detect a transition (often called _edge_ detection) in _software_, we’ll use a `bool` type variable. Let’s see the explanation of how to do this directly in the code:

```c++
#include <Arduino.h>

/*
 * we create a boolean variable outside of the setup and loop functions
 * this way, the variable becomes global
 * a global variable is available in both the setup and loop functions
 * if we had defined the variable inside the setup function, it would only be
 * available in the setup function
 * similarly, if we had defined the variable inside the loop function,
 * it would only be available in the loop function
 */
bool highToLowTransition = false; // by default, its value will be false

void setup()
{
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);   // we set pin 13 as a digital output pin
  digitalWrite(13, LOW); // we ensure the LED is off when the program starts
  pinMode(23, INPUT);    // we set pin 23 as a digital input pin without pullup
}

void loop()
{
  // put your main code here, to run repeatedly:

  if (digitalRead(23) == LOW)
  { // if the button is pressed
    if (highToLowTransition == false)
    { // and it wasn't pressed before

      highToLowTransition = true; // we record that it has been pressed
      // and toggle the LED state
      if (digitalRead(13) == HIGH)
      {                        // if the LED is on
        digitalWrite(13, LOW); // turn it off
      }
      else
      {                         // if it's not on
        digitalWrite(13, HIGH); // turn it on
      }
    }
  }
  else
  {                              // if the button is not pressed
    highToLowTransition = false; // reset the variable to false
  }
}
```

We try again and... bingo! The program works exactly as we wanted. From the previous code, it's important to highlight the [scope property of variables](https://docs.arduino.cc/language-reference/en/variables/variable-scope-qualifiers/scope/). In this case, the variable `highToLowTransition`. The scope of a variable defines where it is available to be read or modified. A variable is available within the function where it is defined. If the variable is defined outside any function, it is known as a global variable, and it becomes available to all functions.

#### _Commit_ of the version

We have a program working correctly. Let's save this version and push it to the remote repository:

```bash
git add {{ platformio_folder_name }}/{{ digital_inputs_project_name }}
git commit -m "the LED turns off and on using the B1 button"
git push
```

#### Pull Request

Once again, create a Pull Request from the `{{ digital_inputs_branch_name }}` branch to `main` and wait for the test results. Correct any undesired behavior detected by the tests, and, once all tests have passed, proceed to merge the Pull Request.

## Challenge

Now let's take it a step further with a challenge for you to complete on your own. In this case, the challenge is to make the LED blink or stop blinking every time we press the B1 button. The LED should initially be off. When we press the B1 button, it should start blinking every 500 ms. When we press the B1 button again, the LED should turn off. With what we know so far, to make the program work correctly, you must keep the button pressed for up to 1 second for the LED to always turn off (and not randomly). **Why?** (We'll see how to fix this in the next session.)

You've seen how to turn on and off an LED, how to make it blink, how to use digital inputs with edge-triggered... you're almost there!

Implement the challenge in a branch called `{{ challenge_branch_name }}` and name the project `{{ challenge_project_name }}`.

### Pull Request

Don't forget to perform the necessary `git add`, `git commit` and `git push` to save the version of the code with the challenge completed!

Once again, create a Pull Request from the `{{ challenge_branch_name }}` branch to `main` and wait for the test results. Correct any undesired behavior detected by the tests, and, once all tests have passed, proceed to merge the Pull Request and enjoy a deserved rest. You have finished the first lab session! 💪

## Evaluation

### Deliverables

These are the elements that should be available to the teaching staff for your evaluation.

- [ ] **Commits**
      Your remote GitHub repository must contain at least the following required commits made during the practice: LED blinking, LED turning on and off with the button, and challenge solution.

- [ ] **Challenge**
      The challenge must be solved and included with its corresponding commit.

- [ ] **Pull Requests**
      The different Pull Requests requested throughout the practice must also be present in your repository.

### Rubric

The rubric we will use for evaluation can be found on CampusVirtual. We recommend that you take a look at it so you know exactly what will be evaluated and what is required.

## Conclusions

In this first practice, we had an initial contact with microcontroller programming.

We saw that any development should be accompanied by a version control system to ensure that validated and functional code is always available. In particular, we saw the use of Git, an open-source VCS with which we cloned a remote GitHub repository to our computer, saved different versions of the code with commits, and shared the code by pushing the changes to the remote repository.

In the code we created, we used digital inputs to generate and read digital signals through the digital GPIOs. We also saw the basic structure of an Arduino project and how to configure the PlatformIO IDE to work with the STM EVB.

Finally, we saw some software-based techniques to generate delays in the program or solve issues with the constant reading of a digital signal generated by a button.
