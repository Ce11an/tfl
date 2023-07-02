# CLI reference

## 📖 Introduction
The TFL CLI provides a command line interface to the TFL API. It is built on top of
[Typer](https://typer.tiangolo.com/), which provides easy way to build command line interfaces. The TFL CLI is bundled
with the [TFL](index.md) package. Once installed, you can use the CLI to access the TFL API.

## ✅ Usage
The TFL CLI is available as `tfl` after installation. You can see the available commands and options by running
`tfl --help`:

```text
 Usage: tfl [OPTIONS] COMMAND [ARGS]...

 tfl: A Python package for the Transport for London (TFL) API.

╭─ Options ──────────────────────────────────────────────────────────────────────────────────╮
│ --version                     Show the version and exit.                                   │
│ --install-completion          Install completion for the current shell.                    │
│ --show-completion             Show completion for the current shell, to copy it or         │
│                               customize the installation.                                  │
│ --help                        Show this message and exit.                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────╮
│ accident-stats    Gets all accident details for accidents occurring in the specified year. │
│ air-quality       Get air quality data feed.                                               │
│ crowding          Information about crowding levels within TFL stations.                   │
│ lift-disruptions  Get current lift disruptions.                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
```

You can also see the available options and arguments for a specific command by running `tfl <command> --help`.
For example:

```bash
tfl lift-disruptions --help
```

which will output:

```text
 Usage: tfl lift-disruptions [OPTIONS] [KEY]

 Get current lift disruptions.

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────╮
│   key      [KEY]  TFL API key. [env var: TFL_API_KEY] [default: None]                      │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
```

### 🔑 Authentication
Anonymous access to the TFL API is limited to 50 requests a minute. You can register for an API key via the TFL API
[website](https://api-portal.tfl.gov.uk/signup). Once you have an API key, you can export it as an environment variable:

```bash
export TFL_API_KEY=<your-api-key>
```

## 📚 Examples

Please note that the below outputs are examples, and the actual output may differ.

### ☁️ Air quality

Get the current TFL air quality, run:
```bash
tfl air-quality
```

which will output:

```text
                              Today's Air Quality
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                       ┃                                                      ┃
┃ Air Pollution Banding ┃ Summary                                              ┃
┃                       ┃                                                      ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                       │                                                      │
│ Low                   │ Low air pollution forecast valid from Tuesday 9 May  │
│                       │ to end of Thursday 11 May GMT                        │
│                       │                                                      │
└───────────────────────┴──────────────────────────────────────────────────────┘
This forecast is intended to provide information on expected pollution levels in
areas of significant public exposure. It may not apply in very specific
locations close to unusually strong or short-lived local sources of pollution.

For more information, please visit: http://londonair.org.uk/forecast

```

### 🛗 Lift disruptions

Get the current TFL lift disruptions, run:
```bash
tfl lift-disruptions
```

which will output:

```text
                              Lift Disruptions
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                             ┃                                             ┃
┃ Station                     ┃ Message                                     ┃
┃                             ┃                                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                             │                                             │
│ Caledonian Road & Barnsbury │ Step free access is not available due to a  │
│                             │ faulty lift. Call us on 0343 222 1234 if    │
│                             │ you need help planning your journey.        │
│                             │                                             │
│                             │                                             │
│ Denmark Hill                │ Step free access is not available to the    │
│                             │ northbound platform due to a faulty lift.   │
│                             │ Call us on 0343 222 1234 if you need help   │
│                             │ planning your journey.                      │
│                             │                                             │
└─────────────────────────────┴─────────────────────────────────────────────┘
                        Current TFL lift disruptions.
```
