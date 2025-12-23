name: Build APK
on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Build with Buildozer
        uses: ArtemGr/buildozer-action@v1
        with:
          buildozer_version: stable
          command: android debug
