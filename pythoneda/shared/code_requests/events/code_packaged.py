# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/events/code_packaged.py

This file declares the CodePackaged class.

Copyright (C) 2023-today rydnr's pythoneda-shared-code-requests/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared import Event, primary_key_attribute
from pythoneda.shared.nix.flake import NixFlake
from typing import List


class CodePackaged(Event):
    """
    Represents the moment code is packaged.

    Class name: CodePackaged

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        nixFlake: NixFlake,
        previousCodeRequestId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new CodePackaged instance.
        :param nixFlake: The Nix flake.
        :type nixFlake: pythoneda.shared.nix.flake.NixFlake
        :param previousCodeRequestId: The id of previous event.
        :type previousCodeRequestId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            [previousCodeRequestId], reconstructedId, reconstructedPreviousEventIds
        )
        self._nix_flake = nixFlake

    @property
    @primary_key_attribute
    def nix_flake(self) -> NixFlake:
        """
        Retrieves the Nix flake.
        :return: Such instance.
        :rtype: pythoneda.shared.nix.flake.NixFlake
        """
        return self._nix_flake


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
