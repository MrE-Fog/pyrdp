#
# This file is part of the PyRDP project.
# Copyright (C) 2018 GoSecure Inc.
# Licensed under the GPLv3 or later.
#

from pyrdp.enum import PlayerPDUType
from pyrdp.enum.player import MouseButton
from pyrdp.pdu.pdu import PDU


class PlayerPDU(PDU):
    """
    PDU to encapsulate different types (ex: input, output, creds) for (re)play purposes.
    Also contains a timestamp.
    """

    def __init__(self, header: PlayerPDUType, timestamp: int, payload: bytes):
        self.header = header  # Uint16LE
        self.timestamp = timestamp  # Uint64LE
        PDU.__init__(self, payload)


class PlayerMouseMovePDU(PlayerPDU):
    """
    PDU definition for mouse move events coming from the player.
    """

    def __init__(self, timestamp: int, x: int, y: int):
        super().__init__(PlayerPDUType.MOUSE_MOVE, timestamp, b"")
        self.x = x
        self.y = y


class PlayerMouseButtonPDU(PlayerPDU):
    """
    PDU definition for mouse button events coming from the player.
    """

    def __init__(self, timestamp: int, x: int, y: int, button: MouseButton, pressed: bool):
        super().__init__(PlayerPDUType.MOUSE_BUTTON, timestamp, b"")
        self.x = x
        self.y = y
        self.button = button
        self.pressed = pressed


class PlayerMouseWheelPDU(PlayerPDU):
    """
    PDU definition for mouse wheel events coming from the player.
    """

    def __init__(self, timestamp: int, x: int, y: int, delta: int, horizontal: bool):
        super().__init__(PlayerPDUType.MOUSE_WHEEL, timestamp, b"")
        self.x = x
        self.y = y
        self.delta = delta
        self.horizontal = horizontal


class PlayerKeyboardPDU(PlayerPDU):
    """
    PDU definition for keyboard events coming from the player.
    """

    def __init__(self, timestamp: int, code: int, released: bool, extended: bool):
        super().__init__(PlayerPDUType.KEYBOARD, timestamp, b"")
        self.code = code
        self.released = released
        self.extended = extended


class PlayerTextPDU(PlayerPDU):
    """
    PDU definition for text events coming from the player.
    """

    def __init__(self, timestamp: int, character: str, released: bool):
        super().__init__(PlayerPDUType.TEXT, timestamp, b"")
        self.character = character
        self.released = released


class PlayerForwardingStatePDU(PlayerPDU):
    """
    PDU definition for changing the state of I/O forwarding.
    """

    def __init__(self, timestamp: int, forwardInput: bool, forwardOutput: bool):
        super().__init__(PlayerPDUType.FORWARDING_STATE, timestamp, b"")
        self.forwardInput = forwardInput
        self.forwardOutput = forwardOutput


class Color:
    def __init__(self, r: int, g: int, b: int, a: int):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

class PlayerBitmapPDU(PlayerPDU):
    """
    PDU definition for bitmap events.
    """

    def __init__(self, timestamp: int, width: int, height: int, pixels: [Color]):
        """
        :param timestamp: timestamp.
        :param width: bitmap width.
        :param height: bitmap height.
        :param pixels: Array of colors organized in a left to right, top to bottom fashion: [(x0, y0), (x1, y0), ..., (x0, y1), (x1, y1)].
        """

        super().__init__(PlayerPDUType.BITMAP, timestamp, b"")
        self.width = width
        self.height = height
        self.pixels = pixels