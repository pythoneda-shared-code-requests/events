"""
pythoneda/shared/code_requests/events/code_execution_requested.py

This file declares the CodeExecutionRequested class.

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
from pythoneda import Event, primary_key_attribute
from pythoneda.shared.code_requests import CodeRequest
from typing import List


class CodeExecutionRequested(Event):
    """
    Represents the moment someone requests to execute some code.

    Class name: CodeExecutionRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        codeRequest: CodeRequest,
        previousCodeRequestId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new CodeExecutionRequested instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
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
        self._code_request = codeRequest

    @property
    @primary_key_attribute
    def code_request(self) -> CodeRequest:
        """
        Retrieves the code request.
        :return: Such instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return self._code_request
