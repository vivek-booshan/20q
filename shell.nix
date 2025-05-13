with import <nixpkgs> {};

mkShell {
  buildInputs = [
    # go
    # gopls
    uv
  ];

  # shellHook = ''
  #   export GO111MODULE=on
  #   if [ ! -f go.mod ] || [ ! -f go.sum ]; then
  #     echo "🔧 go.mod or go.sum not found. Initializing Go module and installing playwright-go..."
  #     go mod init example.com/auto-init || true
  #     go get github.com/playwright-community/playwright-go@latest
  #   else
  #     echo "go.mod and go.sum found. Skipping setup."
  #   fi
  # '';
}

