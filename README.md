# events

Events related to code requests.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-code-requests/events-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-code-requests-events = {
      [optional follows]
      url =
        "github:pythoneda-shared-code-requests/events-artifact/[version]?dir=events";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-code-requests/events-artifact/tree/main/artifact-events](events "events") folder of <https://github.com/pythoneda-shared-code-requests/events-artifact>.


