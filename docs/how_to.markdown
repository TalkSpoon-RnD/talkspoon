---
layout: post
title:  "How To?"
date:   2023-02-26 00:46:00 +0800
permalink: /how-to/
---
## Wellcome to TalkSpoon!

Here are the steps to contribute a prompt to TalkSpoon by creating a Markdown file under a specified category directory and submitting a pull request (PR) on GitHub:

1. First, you need to have a GitHub account and log in.

2. Open the TalkSpoon project [repository page](https://github.com/TalkSpoon-RnD/talkspoon).

3. At the top of the page, click on the "Fork" button to copy the TalkSpoon project code repository to your own GitHub account.

4. Enter the `docs/prompts` directory, where you will see a list of subdirectories, each corresponding to a category of prompts in TalkSpoon. Choose the subdirectory that corresponds to the theme of your prompt.

5. Create a new Markdown file in the subdirectory with a filename following this format:`YEAR-MONTH-DAY-title.md`. For example, a file named `2023-02-26-my-new-prompt.md`

6. Add your prompt to the file. Each prompt should be formatted in one of the following ways:
  
    ```
    ---
    layout: post
    title:  "My New Prompt For xxx"
    date:   2023-02-26 00:46:00 +0800
    ---

    ## [prompt content]

    [prompt description or related information]
    ```

    ```
    ---
    layout: post
    title:  "My New Prompt For xxx"
    date:   2023-02-26 00:46:00 +0800
    ---

    ## [prompt content]

    **Source:** [prompt source]

    [prompt description or related information]
    ```

7. Save the file and commit your changes, which will push your modifications to your TalkSpoon code repository.

8. Next, you need to submit a Pull Request (PR) to merge your changes into the main TalkSpoon codebase. On your code repository page, click the "New Pull Request" button and follow the instructions.

9. If you need more information on how to format your Markdown file or anything related to Jekyll, you can check the [Jekyll documentation](https://jekyllrb.com/docs/home)  for more details.


Once your PR is reviewed and accepted, your prompt will be merged into the main TalkSpoon codebase and other users can start using it.

Please note that your PR should clearly describe the changes you made and why you think they will contribute to TalkSpoon. If your PR is rejected, you can make modifications based on the feedback and submit the PR again.
