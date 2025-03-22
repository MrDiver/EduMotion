"""

Python bindings for GLFW.
"""
import __future__
from __future__ import annotations
import _ctypes
import collections as collections
import ctypes as ctypes
import functools as functools
import logging as logging
import os as os
from posix import getcwd as _getcwd
import sys as sys
import typing
import warnings as warnings
from . import library
__all__ = ['ACCUM_ALPHA_BITS', 'ACCUM_BLUE_BITS', 'ACCUM_GREEN_BITS', 'ACCUM_RED_BITS', 'ALPHA_BITS', 'ANGLE_PLATFORM_TYPE', 'ANGLE_PLATFORM_TYPE_D3D11', 'ANGLE_PLATFORM_TYPE_D3D9', 'ANGLE_PLATFORM_TYPE_METAL', 'ANGLE_PLATFORM_TYPE_NONE', 'ANGLE_PLATFORM_TYPE_OPENGL', 'ANGLE_PLATFORM_TYPE_OPENGLES', 'ANGLE_PLATFORM_TYPE_VULKAN', 'ANY_PLATFORM', 'ANY_POSITION', 'ANY_RELEASE_BEHAVIOR', 'API_UNAVAILABLE', 'ARROW_CURSOR', 'AUTO_ICONIFY', 'AUX_BUFFERS', 'BLUE_BITS', 'CENTER_CURSOR', 'CLIENT_API', 'COCOA_CHDIR_RESOURCES', 'COCOA_FRAME_NAME', 'COCOA_GRAPHICS_SWITCHING', 'COCOA_MENUBAR', 'COCOA_RETINA_FRAMEBUFFER', 'CONNECTED', 'CONTEXT_CREATION_API', 'CONTEXT_DEBUG', 'CONTEXT_NO_ERROR', 'CONTEXT_RELEASE_BEHAVIOR', 'CONTEXT_REVISION', 'CONTEXT_ROBUSTNESS', 'CONTEXT_VERSION_MAJOR', 'CONTEXT_VERSION_MINOR', 'CROSSHAIR_CURSOR', 'CURSOR', 'CURSOR_CAPTURED', 'CURSOR_DISABLED', 'CURSOR_HIDDEN', 'CURSOR_NORMAL', 'CURSOR_UNAVAILABLE', 'DECORATED', 'DEPTH_BITS', 'DISCONNECTED', 'DONT_CARE', 'DOUBLEBUFFER', 'EGL_CONTEXT_API', 'ERROR_REPORTING', 'FALSE', 'FEATURE_UNAVAILABLE', 'FEATURE_UNIMPLEMENTED', 'FLOATING', 'FOCUSED', 'FOCUS_ON_SHOW', 'FORMAT_UNAVAILABLE', 'GAMEPAD_AXIS_LAST', 'GAMEPAD_AXIS_LEFT_TRIGGER', 'GAMEPAD_AXIS_LEFT_X', 'GAMEPAD_AXIS_LEFT_Y', 'GAMEPAD_AXIS_RIGHT_TRIGGER', 'GAMEPAD_AXIS_RIGHT_X', 'GAMEPAD_AXIS_RIGHT_Y', 'GAMEPAD_BUTTON_A', 'GAMEPAD_BUTTON_B', 'GAMEPAD_BUTTON_BACK', 'GAMEPAD_BUTTON_CIRCLE', 'GAMEPAD_BUTTON_CROSS', 'GAMEPAD_BUTTON_DPAD_DOWN', 'GAMEPAD_BUTTON_DPAD_LEFT', 'GAMEPAD_BUTTON_DPAD_RIGHT', 'GAMEPAD_BUTTON_DPAD_UP', 'GAMEPAD_BUTTON_GUIDE', 'GAMEPAD_BUTTON_LAST', 'GAMEPAD_BUTTON_LEFT_BUMPER', 'GAMEPAD_BUTTON_LEFT_THUMB', 'GAMEPAD_BUTTON_RIGHT_BUMPER', 'GAMEPAD_BUTTON_RIGHT_THUMB', 'GAMEPAD_BUTTON_SQUARE', 'GAMEPAD_BUTTON_START', 'GAMEPAD_BUTTON_TRIANGLE', 'GAMEPAD_BUTTON_X', 'GAMEPAD_BUTTON_Y', 'GLFWError', 'GREEN_BITS', 'HAND_CURSOR', 'HAT_CENTERED', 'HAT_DOWN', 'HAT_LEFT', 'HAT_LEFT_DOWN', 'HAT_LEFT_UP', 'HAT_RIGHT', 'HAT_RIGHT_DOWN', 'HAT_RIGHT_UP', 'HAT_UP', 'HOVERED', 'HRESIZE_CURSOR', 'IBEAM_CURSOR', 'ICONIFIED', 'INVALID_ENUM', 'INVALID_VALUE', 'JOYSTICK_1', 'JOYSTICK_10', 'JOYSTICK_11', 'JOYSTICK_12', 'JOYSTICK_13', 'JOYSTICK_14', 'JOYSTICK_15', 'JOYSTICK_16', 'JOYSTICK_2', 'JOYSTICK_3', 'JOYSTICK_4', 'JOYSTICK_5', 'JOYSTICK_6', 'JOYSTICK_7', 'JOYSTICK_8', 'JOYSTICK_9', 'JOYSTICK_HAT_BUTTONS', 'JOYSTICK_LAST', 'KEY_0', 'KEY_1', 'KEY_2', 'KEY_3', 'KEY_4', 'KEY_5', 'KEY_6', 'KEY_7', 'KEY_8', 'KEY_9', 'KEY_A', 'KEY_APOSTROPHE', 'KEY_B', 'KEY_BACKSLASH', 'KEY_BACKSPACE', 'KEY_C', 'KEY_CAPS_LOCK', 'KEY_COMMA', 'KEY_D', 'KEY_DELETE', 'KEY_DOWN', 'KEY_E', 'KEY_END', 'KEY_ENTER', 'KEY_EQUAL', 'KEY_ESCAPE', 'KEY_F', 'KEY_F1', 'KEY_F10', 'KEY_F11', 'KEY_F12', 'KEY_F13', 'KEY_F14', 'KEY_F15', 'KEY_F16', 'KEY_F17', 'KEY_F18', 'KEY_F19', 'KEY_F2', 'KEY_F20', 'KEY_F21', 'KEY_F22', 'KEY_F23', 'KEY_F24', 'KEY_F25', 'KEY_F3', 'KEY_F4', 'KEY_F5', 'KEY_F6', 'KEY_F7', 'KEY_F8', 'KEY_F9', 'KEY_G', 'KEY_GRAVE_ACCENT', 'KEY_H', 'KEY_HOME', 'KEY_I', 'KEY_INSERT', 'KEY_J', 'KEY_K', 'KEY_KP_0', 'KEY_KP_1', 'KEY_KP_2', 'KEY_KP_3', 'KEY_KP_4', 'KEY_KP_5', 'KEY_KP_6', 'KEY_KP_7', 'KEY_KP_8', 'KEY_KP_9', 'KEY_KP_ADD', 'KEY_KP_DECIMAL', 'KEY_KP_DIVIDE', 'KEY_KP_ENTER', 'KEY_KP_EQUAL', 'KEY_KP_MULTIPLY', 'KEY_KP_SUBTRACT', 'KEY_L', 'KEY_LAST', 'KEY_LEFT', 'KEY_LEFT_ALT', 'KEY_LEFT_BRACKET', 'KEY_LEFT_CONTROL', 'KEY_LEFT_SHIFT', 'KEY_LEFT_SUPER', 'KEY_M', 'KEY_MENU', 'KEY_MINUS', 'KEY_N', 'KEY_NUM_LOCK', 'KEY_O', 'KEY_P', 'KEY_PAGE_DOWN', 'KEY_PAGE_UP', 'KEY_PAUSE', 'KEY_PERIOD', 'KEY_PRINT_SCREEN', 'KEY_Q', 'KEY_R', 'KEY_RIGHT', 'KEY_RIGHT_ALT', 'KEY_RIGHT_BRACKET', 'KEY_RIGHT_CONTROL', 'KEY_RIGHT_SHIFT', 'KEY_RIGHT_SUPER', 'KEY_S', 'KEY_SCROLL_LOCK', 'KEY_SEMICOLON', 'KEY_SLASH', 'KEY_SPACE', 'KEY_T', 'KEY_TAB', 'KEY_U', 'KEY_UNKNOWN', 'KEY_UP', 'KEY_V', 'KEY_W', 'KEY_WORLD_1', 'KEY_WORLD_2', 'KEY_X', 'KEY_Y', 'KEY_Z', 'LOCK_KEY_MODS', 'LOSE_CONTEXT_ON_RESET', 'MAXIMIZED', 'MOD_ALT', 'MOD_CAPS_LOCK', 'MOD_CONTROL', 'MOD_NUM_LOCK', 'MOD_SHIFT', 'MOD_SUPER', 'MOUSE_BUTTON_1', 'MOUSE_BUTTON_2', 'MOUSE_BUTTON_3', 'MOUSE_BUTTON_4', 'MOUSE_BUTTON_5', 'MOUSE_BUTTON_6', 'MOUSE_BUTTON_7', 'MOUSE_BUTTON_8', 'MOUSE_BUTTON_LAST', 'MOUSE_BUTTON_LEFT', 'MOUSE_BUTTON_MIDDLE', 'MOUSE_BUTTON_RIGHT', 'MOUSE_PASSTHROUGH', 'NATIVE_CONTEXT_API', 'NORMALIZE_GAMMA_RAMPS', 'NOT_ALLOWED_CURSOR', 'NOT_INITIALIZED', 'NO_API', 'NO_CURRENT_CONTEXT', 'NO_ERROR', 'NO_RESET_NOTIFICATION', 'NO_ROBUSTNESS', 'NO_WINDOW_CONTEXT', 'OPENGL_ANY_PROFILE', 'OPENGL_API', 'OPENGL_COMPAT_PROFILE', 'OPENGL_CORE_PROFILE', 'OPENGL_DEBUG_CONTEXT', 'OPENGL_ES_API', 'OPENGL_FORWARD_COMPAT', 'OPENGL_PROFILE', 'OSMESA_CONTEXT_API', 'OUT_OF_MEMORY', 'PLATFORM', 'PLATFORM_COCOA', 'PLATFORM_ERROR', 'PLATFORM_NULL', 'PLATFORM_UNAVAILABLE', 'PLATFORM_WAYLAND', 'PLATFORM_WIN32', 'PLATFORM_X11', 'POINTING_HAND_CURSOR', 'POSITION_X', 'POSITION_Y', 'PRESS', 'RAW_MOUSE_MOTION', 'RED_BITS', 'REFRESH_RATE', 'RELEASE', 'RELEASE_BEHAVIOR_FLUSH', 'RELEASE_BEHAVIOR_NONE', 'REPEAT', 'RESIZABLE', 'RESIZE_ALL_CURSOR', 'RESIZE_EW_CURSOR', 'RESIZE_NESW_CURSOR', 'RESIZE_NS_CURSOR', 'RESIZE_NWSE_CURSOR', 'SAMPLES', 'SCALE_FRAMEBUFFER', 'SCALE_TO_MONITOR', 'SRGB_CAPABLE', 'STENCIL_BITS', 'STEREO', 'STICKY_KEYS', 'STICKY_MOUSE_BUTTONS', 'TRANSPARENT_FRAMEBUFFER', 'TRUE', 'VERSION_MAJOR', 'VERSION_MINOR', 'VERSION_REVISION', 'VERSION_UNAVAILABLE', 'VISIBLE', 'VRESIZE_CURSOR', 'WAYLAND_APP_ID', 'WAYLAND_DISABLE_LIBDECOR', 'WAYLAND_LIBDECOR', 'WAYLAND_PREFER_LIBDECOR', 'WIN32_KEYBOARD_MENU', 'WIN32_SHOWDEFAULT', 'X11_CLASS_NAME', 'X11_INSTANCE_NAME', 'X11_XCB_VULKAN_SURFACE', 'collections', 'create_cursor', 'create_standard_cursor', 'create_window', 'create_window_surface', 'ctypes', 'default_window_hints', 'destroy_cursor', 'destroy_window', 'division', 'extension_supported', 'focus_window', 'functools', 'get_clipboard_string', 'get_current_context', 'get_cursor_pos', 'get_egl_context', 'get_egl_display', 'get_egl_surface', 'get_error', 'get_framebuffer_size', 'get_gamepad_name', 'get_gamepad_state', 'get_gamma_ramp', 'get_glx_context', 'get_glx_window', 'get_input_mode', 'get_instance_proc_address', 'get_joystick_axes', 'get_joystick_buttons', 'get_joystick_guid', 'get_joystick_hats', 'get_joystick_name', 'get_joystick_user_pointer', 'get_key', 'get_key_name', 'get_key_scancode', 'get_monitor_content_scale', 'get_monitor_name', 'get_monitor_physical_size', 'get_monitor_pos', 'get_monitor_user_pointer', 'get_monitor_workarea', 'get_monitors', 'get_mouse_button', 'get_os_mesa_color_buffer', 'get_os_mesa_context', 'get_os_mesa_depth_buffer', 'get_physical_device_presentation_support', 'get_platform', 'get_primary_monitor', 'get_proc_address', 'get_required_instance_extensions', 'get_time', 'get_timer_frequency', 'get_timer_value', 'get_version', 'get_version_string', 'get_video_mode', 'get_video_modes', 'get_wayland_display', 'get_wayland_monitor', 'get_wayland_window', 'get_window_attrib', 'get_window_content_scale', 'get_window_frame_size', 'get_window_monitor', 'get_window_opacity', 'get_window_pos', 'get_window_size', 'get_window_title', 'get_window_user_pointer', 'get_x11_adapter', 'get_x11_display', 'get_x11_monitor', 'get_x11_selection_string', 'get_x11_window', 'hide_window', 'iconify_window', 'init', 'init_allocator', 'init_hint', 'init_vulkan_loader', 'joystick_is_gamepad', 'joystick_present', 'library', 'logging', 'make_context_current', 'maximize_window', 'os', 'platform_supported', 'poll_events', 'post_empty_event', 'print_function', 'raw_mouse_motion_supported', 'request_window_attention', 'restore_window', 'set_char_callback', 'set_char_mods_callback', 'set_clipboard_string', 'set_cursor', 'set_cursor_enter_callback', 'set_cursor_pos', 'set_cursor_pos_callback', 'set_drop_callback', 'set_error_callback', 'set_framebuffer_size_callback', 'set_gamma', 'set_gamma_ramp', 'set_input_mode', 'set_joystick_callback', 'set_joystick_user_pointer', 'set_key_callback', 'set_monitor_callback', 'set_monitor_user_pointer', 'set_mouse_button_callback', 'set_scroll_callback', 'set_time', 'set_window_aspect_ratio', 'set_window_attrib', 'set_window_close_callback', 'set_window_content_scale_callback', 'set_window_focus_callback', 'set_window_icon', 'set_window_iconify_callback', 'set_window_maximize_callback', 'set_window_monitor', 'set_window_opacity', 'set_window_pos', 'set_window_pos_callback', 'set_window_refresh_callback', 'set_window_should_close', 'set_window_size', 'set_window_size_callback', 'set_window_size_limits', 'set_window_title', 'set_window_user_pointer', 'set_x11_selection_string', 'show_window', 'swap_buffers', 'swap_interval', 'sys', 'terminate', 'unicode_literals', 'update_gamepad_mappings', 'vulkan_supported', 'wait_events', 'wait_events_timeout', 'warnings', 'window_hint', 'window_hint_string', 'window_should_close']
class GLFWError(UserWarning):
    """
    
        Exception class used for reporting GLFW errors.
        
    """
    def __init__(self, message, error_code = None):
        ...
class _GLFWallocator(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWallocator GLFWallocator;
        
    """
    _fields_: typing.ClassVar[list] = [('allocate', ctypes.CFUNCTYPE.<locals>.CFunctionType), ('reallocate', ctypes.CFUNCTYPE.<locals>.CFunctionType), ('deallocate', ctypes.CFUNCTYPE.<locals>.CFunctionType)]
class _GLFWcursor(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWcursor GLFWcursor;
        
    """
    _fields_: typing.ClassVar[list] = [('dummy', ctypes.c_int)]
class _GLFWgamepadstate(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWgamepadstate GLFWgamepadstate;
        
    """
    class GLFWgamepadstate(tuple):
        """
        GLFWgamepadstate(buttons, axes)
        """
        __match_args__: typing.ClassVar[tuple] = ('buttons', 'axes')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('buttons', 'axes')
        @staticmethod
        def __new__(_cls, buttons, axes):
            """
            Create new instance of GLFWgamepadstate(buttons, axes)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new GLFWgamepadstate object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new GLFWgamepadstate object replacing specified fields with new values
            """
    _fields_: typing.ClassVar[list] = [('buttons', c_ubyte_Array_15), ('axes', c_float_Array_6)]
    def __init__(self):
        ...
    def unwrap(self):
        """
        
                Returns a GLFWvidmode object.
                
        """
    def wrap(self, gamepad_state):
        """
        
                Wraps a nested python sequence.
                
        """
class _GLFWgammaramp(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWgammaramp GLFWgammaramp;
        
    """
    class GLFWgammaramp(tuple):
        """
        GLFWgammaramp(red, green, blue)
        """
        __match_args__: typing.ClassVar[tuple] = ('red', 'green', 'blue')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('red', 'green', 'blue')
        @staticmethod
        def __new__(_cls, red, green, blue):
            """
            Create new instance of GLFWgammaramp(red, green, blue)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new GLFWgammaramp object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new GLFWgammaramp object replacing specified fields with new values
            """
    _fields_: typing.ClassVar[list] = [('red', LP_c_ushort), ('green', LP_c_ushort), ('blue', LP_c_ushort), ('size', ctypes.c_uint)]
    def __init__(self):
        ...
    def unwrap(self):
        """
        
                Returns a GLFWgammaramp object.
                
        """
    def wrap(self, gammaramp):
        """
        
                Wraps a nested python sequence.
                
        """
class _GLFWimage(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWimage GLFWimage;
        
    """
    class GLFWimage(tuple):
        """
        GLFWimage(width, height, pixels)
        """
        __match_args__: typing.ClassVar[tuple] = ('width', 'height', 'pixels')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('width', 'height', 'pixels')
        @staticmethod
        def __new__(_cls, width, height, pixels):
            """
            Create new instance of GLFWimage(width, height, pixels)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new GLFWimage object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new GLFWimage object replacing specified fields with new values
            """
    _fields_: typing.ClassVar[list] = [('width', ctypes.c_int), ('height', ctypes.c_int), ('pixels', LP_c_ubyte)]
    def __init__(self):
        ...
    def unwrap(self):
        """
        
                Returns a GLFWimage object.
                
        """
    def wrap(self, image):
        """
        
                Wraps a nested python sequence or PIL/pillow Image.
                
        """
class _GLFWmonitor(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWmonitor GLFWmonitor;
        
    """
    _fields_: typing.ClassVar[list] = [('dummy', ctypes.c_int)]
class _GLFWvidmode(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWvidmode GLFWvidmode;
        
    """
    class Bits(tuple):
        """
        Bits(red, green, blue)
        """
        __match_args__: typing.ClassVar[tuple] = ('red', 'green', 'blue')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('red', 'green', 'blue')
        @staticmethod
        def __new__(_cls, red, green, blue):
            """
            Create new instance of Bits(red, green, blue)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new Bits object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new Bits object replacing specified fields with new values
            """
    class GLFWvidmode(tuple):
        """
        GLFWvidmode(size, bits, refresh_rate)
        """
        __match_args__: typing.ClassVar[tuple] = ('size', 'bits', 'refresh_rate')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('size', 'bits', 'refresh_rate')
        @staticmethod
        def __new__(_cls, size, bits, refresh_rate):
            """
            Create new instance of GLFWvidmode(size, bits, refresh_rate)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new GLFWvidmode object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new GLFWvidmode object replacing specified fields with new values
            """
    class Size(tuple):
        """
        Size(width, height)
        """
        __match_args__: typing.ClassVar[tuple] = ('width', 'height')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('width', 'height')
        @staticmethod
        def __new__(_cls, width, height):
            """
            Create new instance of Size(width, height)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new Size object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new Size object replacing specified fields with new values
            """
    _fields_: typing.ClassVar[list] = [('width', ctypes.c_int), ('height', ctypes.c_int), ('red_bits', ctypes.c_int), ('green_bits', ctypes.c_int), ('blue_bits', ctypes.c_int), ('refresh_rate', ctypes.c_uint)]
    def __init__(self):
        ...
    def unwrap(self):
        """
        
                Returns a GLFWvidmode object.
                
        """
    def wrap(self, video_mode):
        """
        
                Wraps a nested python sequence.
                
        """
class _GLFWwindow(_ctypes.Structure):
    """
    
        Wrapper for:
            typedef struct GLFWwindow GLFWwindow;
        
    """
    _fields_: typing.ClassVar[list] = [('dummy', ctypes.c_int)]
def _callback_exception_decorator(func):
    ...
def _handle_glfw_errors(*args, **kwargs):
    """
    
        Default error callback that raises GLFWError exceptions, issues GLFWError
        warnings or logs to the 'glfw' logger.
        Set an alternative error callback or set glfw.ERROR_REPORTING to False or
        'ignore' to disable this behavior.
        
    """
def _prepare_errcheck():
    """
    
        This function sets the errcheck attribute of all ctypes wrapped functions
        to evaluate the _exc_info_from_callback global variable and re-raise any
        exceptions that might have been raised in callbacks.
        It also modifies all callback types to automatically wrap the function
        using the _callback_exception_decorator.
        
    """
def _reraise(exception, traceback):
    ...
def create_cursor(image, xhot, yhot):
    """
    
            Creates a custom cursor.
    
            Wrapper for:
                GLFWcursor* glfwCreateCursor(const GLFWimage* image, int xhot, int yhot);
            
    """
def create_standard_cursor(shape):
    """
    
            Creates a cursor with a standard shape.
    
            Wrapper for:
                GLFWcursor* glfwCreateStandardCursor(int shape);
            
    """
def create_window(width, height, title, monitor, share):
    """
    
        Creates a window and its associated context.
    
        Wrapper for:
            GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);
        
    """
def create_window_surface(instance, window, allocator, surface):
    """
    
            Creates a Vulkan surface for the specified window.
    
            Wrapper for:
                VkResult glfwCreateWindowSurface(VkInstance instance, GLFWwindow* window, const VkAllocationCallbacks* allocator, VkSurfaceKHR* surface);
            
    """
def default_window_hints():
    """
    
        Resets all window hints to their default values.
    
        Wrapper for:
            void glfwDefaultWindowHints(void);
        
    """
def destroy_cursor(cursor):
    """
    
            Destroys a cursor.
    
            Wrapper for:
                void glfwDestroyCursor(GLFWcursor* cursor);
            
    """
def destroy_window(window):
    """
    
        Destroys the specified window and its context.
    
        Wrapper for:
            void glfwDestroyWindow(GLFWwindow* window);
        
    """
def extension_supported(extension):
    """
    
        Returns whether the specified extension is available.
    
        Wrapper for:
            int glfwExtensionSupported(const char* extension);
        
    """
def focus_window(window):
    """
    
            Brings the specified window to front and sets input focus.
    
            Wrapper for:
                void glfwFocusWindow(GLFWwindow* window);
            
    """
def get_clipboard_string(window):
    """
    
        Retrieves the contents of the clipboard as a string.
    
        Wrapper for:
            const char* glfwGetClipboardString(GLFWwindow* window);
        
    """
def get_current_context():
    """
    
        Returns the window whose context is current on the calling thread.
    
        Wrapper for:
            GLFWwindow* glfwGetCurrentContext(void);
        
    """
def get_cursor_pos(window):
    """
    
        Retrieves the last reported cursor position, relative to the client
        area of the window.
    
        Wrapper for:
            void glfwGetCursorPos(GLFWwindow* window, double* xpos, double* ypos);
        
    """
def get_egl_context(window):
    """
    
            Returns the EGLContext of the specified window.
    
            Wrapper for:
                EGLContext glfwGetEGLContext(GLFWwindow* window);
            
    """
def get_egl_display():
    """
    
            Returns the EGLDisplay used by GLFW.
    
            Wrapper for:
                EGLDisplay glfwGetEGLDisplay(void);
            
    """
def get_egl_surface(window):
    """
    
            Returns the EGLSurface of the specified window.
    
            Wrapper for:
                EGLSurface glfwGetEGLSurface(GLFWwindow* window);
            
    """
def get_error():
    """
    
            Returns and clears the last error for the calling thread.
    
            Wrapper for:
                int glfwGetError(const char** description);
            
    """
def get_framebuffer_size(window):
    """
    
        Retrieves the size of the framebuffer of the specified window.
    
        Wrapper for:
            void glfwGetFramebufferSize(GLFWwindow* window, int* width, int* height);
        
    """
def get_gamepad_name(joystick_id):
    """
    
            Returns the human-readable gamepad name for the specified joystick.
    
            Wrapper for:
                const char* glfwGetGamepadName(int jid);
            
    """
def get_gamepad_state(joystick_id):
    """
    
            Retrieves the state of the specified joystick remapped as a gamepad.
    
            Wrapper for:
                int glfwGetGamepadState(int jid, GLFWgamepadstate* state);
            
    """
def get_gamma_ramp(monitor):
    """
    
        Retrieves the current gamma ramp for the specified monitor.
    
        Wrapper for:
            const GLFWgammaramp* glfwGetGammaRamp(GLFWmonitor* monitor);
        
    """
def get_glx_context(window):
    """
    
            Returns the GLXContext of the specified window.
    
            Wrapper for:
                GLXContext glfwGetGLXContext(GLFWwindow* window);
            
    """
def get_glx_window(window):
    """
    
            Returns the GLXWindow of the specified window.
    
            Wrapper for:
                GLXWindow glfwGetGLXWindow(GLFWwindow* window);
            
    """
def get_input_mode(window, mode):
    """
    
        Returns the value of an input option for the specified window.
    
        Wrapper for:
            int glfwGetInputMode(GLFWwindow* window, int mode);
        
    """
def get_instance_proc_address(instance, procname):
    """
    
            Returns the address of the specified Vulkan instance function.
    
            Wrapper for:
                GLFWvkproc glfwGetInstanceProcAddress(VkInstance instance, const char* procname);
            
    """
def get_joystick_axes(joy):
    """
    
        Returns the values of all axes of the specified joystick.
    
        Wrapper for:
            const float* glfwGetJoystickAxes(int joy, int* count);
        
    """
def get_joystick_buttons(joy):
    """
    
        Returns the state of all buttons of the specified joystick.
    
        Wrapper for:
            const unsigned char* glfwGetJoystickButtons(int joy, int* count);
        
    """
def get_joystick_guid(joystick_id):
    """
    
            Returns the SDL compatible GUID of the specified joystick.
    
            Wrapper for:
                const char* glfwGetJoystickGUID(int jid);
            
    """
def get_joystick_hats(joystick_id):
    """
    
            Returns the state of all hats of the specified joystick.
    
            Wrapper for:
                const unsigned char* glfwGetJoystickButtons(int joy, int* count);
            
    """
def get_joystick_name(joy):
    """
    
        Returns the name of the specified joystick.
    
        Wrapper for:
            const char* glfwGetJoystickName(int joy);
        
    """
def get_joystick_user_pointer(joystick_id):
    """
    
            Returns the user pointer of the specified joystick.
    
            Wrapper for:
                void* glfwGetJoystickUserPointer(int jid);
            
    """
def get_key(window, key):
    """
    
        Returns the last reported state of a keyboard key for the specified
        window.
    
        Wrapper for:
            int glfwGetKey(GLFWwindow* window, int key);
        
    """
def get_key_name(key, scancode):
    """
    
            Returns the localized name of the specified printable key.
    
            Wrapper for:
                const char* glfwGetKeyName(int key, int scancode);
            
    """
def get_key_scancode(key):
    """
    
            Returns the platform-specific scancode of the specified key.
    
            Wrapper for:
                int glfwGetKeyScancode(int key);
            
    """
def get_monitor_content_scale(monitor):
    """
    
            Retrieves the content scale for the specified monitor.
    
            Wrapper for:
                void glfwGetMonitorContentScale(GLFWmonitor* monitor, float* xscale, float* yscale);
            
    """
def get_monitor_name(monitor):
    """
    
        Returns the name of the specified monitor.
    
        Wrapper for:
            const char* glfwGetMonitorName(GLFWmonitor* monitor);
        
    """
def get_monitor_physical_size(monitor):
    """
    
        Returns the physical size of the monitor.
    
        Wrapper for:
            void glfwGetMonitorPhysicalSize(GLFWmonitor* monitor, int* width, int* height);
        
    """
def get_monitor_pos(monitor):
    """
    
        Returns the position of the monitor's viewport on the virtual screen.
    
        Wrapper for:
            void glfwGetMonitorPos(GLFWmonitor* monitor, int* xpos, int* ypos);
        
    """
def get_monitor_user_pointer(monitor):
    """
    
            Returns the user pointer of the specified monitor.
    
            Wrapper for:
                void* glfwGetMonitorUserPointer(int jid);
            
    """
def get_monitor_workarea(monitor):
    """
    
            Retrives the work area of the monitor.
    
            Wrapper for:
                void glfwGetMonitorWorkarea(GLFWmonitor* monitor, int* xpos, int* ypos, int* width, int* height);
            
    """
def get_monitors():
    """
    
        Returns the currently connected monitors.
    
        Wrapper for:
            GLFWmonitor** glfwGetMonitors(int* count);
        
    """
def get_mouse_button(window, button):
    """
    
        Returns the last reported state of a mouse button for the specified
        window.
    
        Wrapper for:
            int glfwGetMouseButton(GLFWwindow* window, int button);
        
    """
def get_os_mesa_color_buffer(window):
    """
    
            Retrieves the color buffer associated with the specified window.
    
            Wrapper for:
                int glfwGetOSMesaColorBuffer(GLFWwindow* window, int* width, int* height, int* format, void** buffer);
            
    """
def get_os_mesa_context(window):
    """
    
            Returns the OSMesaContext of the specified window.
    
            Wrapper for:
                OSMesaContext glfwGetOSMesaContext(GLFWwindow* window);
            
    """
def get_os_mesa_depth_buffer(window):
    """
    
            Retrieves the depth buffer associated with the specified window.
    
            Wrapper for:
                int glfwGetOSMesaDepthBuffer(GLFWwindow* window, int* width, int* height, int* bytesPerValue, void** buffer);
            
    """
def get_physical_device_presentation_support(instance, device, queuefamily):
    """
    
            Creates a Vulkan surface for the specified window.
    
            Wrapper for:
                int glfwGetPhysicalDevicePresentationSupport(VkInstance instance, VkPhysicalDevice device, uint32_t queuefamily);
            
    """
def get_platform():
    """
    
            Returns the currently selected platform.
    
            Wrapper for:
                int glfwGetPlatform(void);
            
    """
def get_primary_monitor():
    """
    
        Returns the primary monitor.
    
        Wrapper for:
            GLFWmonitor* glfwGetPrimaryMonitor(void);
        
    """
def get_proc_address(procname):
    """
    
        Returns the address of the specified function for the current
        context.
    
        Wrapper for:
            GLFWglproc glfwGetProcAddress(const char* procname);
        
    """
def get_required_instance_extensions():
    """
    
            Returns the Vulkan instance extensions required by GLFW.
    
            Wrapper for:
                const char** glfwGetRequiredInstanceExtensions(uint32_t* count);
            
    """
def get_time():
    """
    
        Returns the value of the GLFW timer.
    
        Wrapper for:
            double glfwGetTime(void);
        
    """
def get_timer_frequency():
    """
    
            Returns the frequency, in Hz, of the raw timer.
    
            Wrapper for:
                uint64_t glfwGetTimerFrequency(void);
            
    """
def get_timer_value():
    """
    
            Returns the current value of the raw timer.
    
            Wrapper for:
                uint64_t glfwGetTimerValue(void);
            
    """
def get_version():
    """
    
        Retrieves the version of the GLFW library.
    
        Wrapper for:
            void glfwGetVersion(int* major, int* minor, int* rev);
        
    """
def get_version_string():
    """
    
        Returns a string describing the compile-time configuration.
    
        Wrapper for:
            const char* glfwGetVersionString(void);
        
    """
def get_video_mode(monitor):
    """
    
        Returns the current mode of the specified monitor.
    
        Wrapper for:
            const GLFWvidmode* glfwGetVideoMode(GLFWmonitor* monitor);
        
    """
def get_video_modes(monitor):
    """
    
        Returns the available video modes for the specified monitor.
    
        Wrapper for:
            const GLFWvidmode* glfwGetVideoModes(GLFWmonitor* monitor, int* count);
        
    """
def get_wayland_display():
    """
    
            Returns the struct wl_display* used by GLFW.
    
            Wrapper for:
                struct wl_display* glfwGetWaylandDisplay(void);
            
    """
def get_wayland_monitor(monitor):
    """
    
            Returns the struct wl_output* of the specified monitor.
    
            Wrapper for:
                struct wl_output* glfwGetWaylandMonitor(GLFWmonitor* monitor);
            
    """
def get_wayland_window(window):
    """
    
            Returns the main struct wl_surface* of the specified window.
    
            Wrapper for:
                struct wl_surface* glfwGetWaylandWindow(GLFWwindow* window);
            
    """
def get_window_attrib(window, attrib):
    """
    
        Returns an attribute of the specified window.
    
        Wrapper for:
            int glfwGetWindowAttrib(GLFWwindow* window, int attrib);
        
    """
def get_window_content_scale(window):
    """
    
            Retrieves the content scale for the specified window.
    
            Wrapper for:
                void glfwGetWindowContentScale(GLFWwindow* window, float* xscale, float* yscale);
            
    """
def get_window_frame_size(window):
    """
    
            Retrieves the size of the frame of the window.
    
            Wrapper for:
                void glfwGetWindowFrameSize(GLFWwindow* window, int* left, int* top, int* right, int* bottom);
            
    """
def get_window_monitor(window):
    """
    
        Returns the monitor that the window uses for full screen mode.
    
        Wrapper for:
            GLFWmonitor* glfwGetWindowMonitor(GLFWwindow* window);
        
    """
def get_window_opacity(window):
    """
    
            Returns the opacity of the whole window.
    
            Wrapper for:
                float glfwGetWindowOpacity(GLFWwindow* window);
            
    """
def get_window_pos(window):
    """
    
        Retrieves the position of the client area of the specified window.
    
        Wrapper for:
            void glfwGetWindowPos(GLFWwindow* window, int* xpos, int* ypos);
        
    """
def get_window_size(window):
    """
    
        Retrieves the size of the client area of the specified window.
    
        Wrapper for:
            void glfwGetWindowSize(GLFWwindow* window, int* width, int* height);
        
    """
def get_window_title(window):
    """
    
            Returns the title of the specified window.
    
            Wrapper for:
                const char* glfwGetWindowTitle(GLFWwindow* window);
            
    """
def get_window_user_pointer(window):
    """
    
        Returns the user pointer of the specified window.
    
        Wrapper for:
            void* glfwGetWindowUserPointer(GLFWwindow* window);
        
    """
def get_x11_adapter(monitor):
    """
    
            Returns the RRCrtc of the specified monitor.
    
            Wrapper for:
                RRCrtc glfwGetX11Adapter(GLFWmonitor* monitor);
            
    """
def get_x11_display():
    """
    
            Returns the Display used by GLFW.
    
            Wrapper for:
                Display* glfwGetX11Display(void);
            
    """
def get_x11_monitor(monitor):
    """
    
            Returns the RROutput of the specified monitor.
    
            Wrapper for:
                RROutput glfwGetX11Monitor(GLFWmonitor* monitor);
            
    """
def get_x11_selection_string():
    """
    
            Returns the contents of the current primary selection as a string.
    
            Wrapper for:
                const char* glfwGetX11SelectionString(void);
            
    """
def get_x11_window(window):
    """
    
            Returns the Window of the specified window.
    
            Wrapper for:
                Window glfwGetX11Window(GLFWwindow* window);
            
    """
def hide_window(window):
    """
    
        Hides the specified window.
    
        Wrapper for:
            void glfwHideWindow(GLFWwindow* window);
        
    """
def iconify_window(window):
    """
    
        Iconifies the specified window.
    
        Wrapper for:
            void glfwIconifyWindow(GLFWwindow* window);
        
    """
def init():
    """
    
        Initializes the GLFW library.
    
        Wrapper for:
            int glfwInit(void);
        
    """
def init_allocator(allocate, reallocate, deallocate):
    """
    
            Sets the init allocator to the desired value.
    
            Wrapper for:
                void glfwInitAllocator(const GLFWallocator* allocator);
            
    """
def init_hint(hint, value):
    """
    
            Sets the specified init hint to the desired value.
    
            Wrapper for:
                void glfwInitHint(int hint, int value);
            
    """
def init_vulkan_loader(loader):
    """
    
            Sets the desired Vulkan `vkGetInstanceProcAddr` function.
    
            Wrapper for:
                void glfwInitVulkanLoader(PFN_vkGetInstanceProcAddr loader);
            
    """
def joystick_is_gamepad(joystick_id):
    """
    
            Returns whether the specified joystick has a gamepad mapping.
    
            Wrapper for:
                int glfwJoystickIsGamepad(int jid);
            
    """
def joystick_present(joy):
    """
    
        Returns whether the specified joystick is present.
    
        Wrapper for:
            int glfwJoystickPresent(int joy);
        
    """
def make_context_current(window):
    """
    
        Makes the context of the specified window current for the calling
        thread.
    
        Wrapper for:
            void glfwMakeContextCurrent(GLFWwindow* window);
        
    """
def maximize_window(window):
    """
    
            Maximizes the specified window.
    
            Wrapper for:
                void glfwMaximizeWindow(GLFWwindow* window);
            
    """
def platform_supported(platform):
    """
    
            Returns whether the library includes support for the specified platform.
    
            Wrapper for:
                int glfwPlatformSupported(int platform);
            
    """
def poll_events():
    """
    
        Processes all pending events.
    
        Wrapper for:
            void glfwPollEvents(void);
        
    """
def post_empty_event():
    """
    
            Posts an empty event to the event queue.
    
            Wrapper for:
                void glfwPostEmptyEvent();
            
    """
def raw_mouse_motion_supported():
    """
    
            Returns whether raw mouse motion is supported.
    
            Wrapper for:
                int glfwRawMouseMotionSupported(void);
            
    """
def request_window_attention(window):
    """
    
            Requests user attention to the specified window.
    
            Wrapper for:
                void glfwRequestWindowAttention(GLFWwindow* window);
            
    """
def restore_window(window):
    """
    
        Restores the specified window.
    
        Wrapper for:
            void glfwRestoreWindow(GLFWwindow* window);
        
    """
def set_char_callback(window, cbfun):
    """
    
        Sets the Unicode character callback.
    
        Wrapper for:
            GLFWcharfun glfwSetCharCallback(GLFWwindow* window, GLFWcharfun cbfun);
        
    """
def set_char_mods_callback(window, cbfun):
    """
    
            Sets the Unicode character with modifiers callback.
    
            Wrapper for:
                GLFWcharmodsfun glfwSetCharModsCallback(GLFWwindow* window, GLFWcharmodsfun cbfun);
            
    """
def set_clipboard_string(window, string):
    """
    
        Sets the clipboard to the specified string.
    
        Wrapper for:
            void glfwSetClipboardString(GLFWwindow* window, const char* string);
        
    """
def set_cursor(window, cursor):
    """
    
            Sets the cursor for the window.
    
            Wrapper for:
                void glfwSetCursor(GLFWwindow* window, GLFWcursor* cursor);
            
    """
def set_cursor_enter_callback(window, cbfun):
    """
    
        Sets the cursor enter/exit callback.
    
        Wrapper for:
            GLFWcursorenterfun glfwSetCursorEnterCallback(GLFWwindow* window, GLFWcursorenterfun cbfun);
        
    """
def set_cursor_pos(window, xpos, ypos):
    """
    
        Sets the position of the cursor, relative to the client area of the window.
    
        Wrapper for:
            void glfwSetCursorPos(GLFWwindow* window, double xpos, double ypos);
        
    """
def set_cursor_pos_callback(window, cbfun):
    """
    
        Sets the cursor position callback.
    
        Wrapper for:
            GLFWcursorposfun glfwSetCursorPosCallback(GLFWwindow* window, GLFWcursorposfun cbfun);
        
    """
def set_drop_callback(window, cbfun):
    """
    
            Sets the file drop callback.
    
            Wrapper for:
                GLFWdropfun glfwSetDropCallback(GLFWwindow* window, GLFWdropfun cbfun);
            
    """
def set_error_callback(cbfun):
    """
    
        Sets the error callback.
    
        Wrapper for:
            GLFWerrorfun glfwSetErrorCallback(GLFWerrorfun cbfun);
        
    """
def set_framebuffer_size_callback(window, cbfun):
    """
    
        Sets the framebuffer resize callback for the specified window.
    
        Wrapper for:
            GLFWframebuffersizefun glfwSetFramebufferSizeCallback(GLFWwindow* window, GLFWframebuffersizefun cbfun);
        
    """
def set_gamma(monitor, gamma):
    """
    
        Generates a gamma ramp and sets it for the specified monitor.
    
        Wrapper for:
            void glfwSetGamma(GLFWmonitor* monitor, float gamma);
        
    """
def set_gamma_ramp(monitor, ramp):
    """
    
        Sets the current gamma ramp for the specified monitor.
    
        Wrapper for:
            void glfwSetGammaRamp(GLFWmonitor* monitor, const GLFWgammaramp* ramp);
        
    """
def set_input_mode(window, mode, value):
    """
    
        Sets an input option for the specified window.
        @param[in] window The window whose input mode to set.
        @param[in] mode One of `GLFW_CURSOR`, `GLFW_STICKY_KEYS` or
        `GLFW_STICKY_MOUSE_BUTTONS`.
        @param[in] value The new value of the specified input mode.
    
        Wrapper for:
            void glfwSetInputMode(GLFWwindow* window, int mode, int value);
        
    """
def set_joystick_callback(cbfun):
    """
    
            Sets the error callback.
    
            Wrapper for:
                GLFWjoystickfun glfwSetJoystickCallback(GLFWjoystickfun cbfun);
            
    """
def set_joystick_user_pointer(joystick_id, pointer):
    """
    
            Sets the user pointer of the specified joystick. You may pass a normal
            python object into this function and it will be wrapped automatically.
            The object will be kept in existence until the pointer is set to
            something else.
    
            Wrapper for:
                void glfwSetJoystickUserPointer(int jid, void* pointer);
            
    """
def set_key_callback(window, cbfun):
    """
    
        Sets the key callback.
    
        Wrapper for:
            GLFWkeyfun glfwSetKeyCallback(GLFWwindow* window, GLFWkeyfun cbfun);
        
    """
def set_monitor_callback(cbfun):
    """
    
        Sets the monitor configuration callback.
    
        Wrapper for:
            GLFWmonitorfun glfwSetMonitorCallback(GLFWmonitorfun cbfun);
        
    """
def set_monitor_user_pointer(monitor, pointer):
    """
    
            Sets the user pointer of the specified monitor. You may pass a normal
            python object into this function and it will be wrapped automatically.
            The object will be kept in existence until the pointer is set to
            something else.
    
            Wrapper for:
                void glfwSetMonitorUserPointer(int jid, void* pointer);
            
    """
def set_mouse_button_callback(window, cbfun):
    """
    
        Sets the mouse button callback.
    
        Wrapper for:
            GLFWmousebuttonfun glfwSetMouseButtonCallback(GLFWwindow* window, GLFWmousebuttonfun cbfun);
        
    """
def set_scroll_callback(window, cbfun):
    """
    
        Sets the scroll callback.
    
        Wrapper for:
            GLFWscrollfun glfwSetScrollCallback(GLFWwindow* window, GLFWscrollfun cbfun);
        
    """
def set_time(time):
    """
    
        Sets the GLFW timer.
    
        Wrapper for:
            void glfwSetTime(double time);
        
    """
def set_window_aspect_ratio(window, numer, denom):
    """
    
            Sets the aspect ratio of the specified window.
    
            Wrapper for:
                void glfwSetWindowAspectRatio(GLFWwindow* window, int numer, int denom);
            
    """
def set_window_attrib(window, attrib, value):
    """
    
            Returns an attribute of the specified window.
    
            Wrapper for:
                void glfwSetWindowAttrib(GLFWwindow* window, int attrib, int value);
            
    """
def set_window_close_callback(window, cbfun):
    """
    
        Sets the close callback for the specified window.
    
        Wrapper for:
            GLFWwindowclosefun glfwSetWindowCloseCallback(GLFWwindow* window, GLFWwindowclosefun cbfun);
        
    """
def set_window_content_scale_callback(window, cbfun):
    """
    
            Sets the window content scale callback for the specified window.
    
            Wrapper for:
                GLFWwindowcontentscalefun glfwSetWindowContentScaleCallback(GLFWwindow* window, GLFWwindowcontentscalefun cbfun);
            
    """
def set_window_focus_callback(window, cbfun):
    """
    
        Sets the focus callback for the specified window.
    
        Wrapper for:
            GLFWwindowfocusfun glfwSetWindowFocusCallback(GLFWwindow* window, GLFWwindowfocusfun cbfun);
        
    """
def set_window_icon(window, count, images):
    """
    
            Sets the icon for the specified window.
    
            Wrapper for:
                void glfwSetWindowIcon(GLFWwindow* window, int count, const GLFWimage* images);
            
    """
def set_window_iconify_callback(window, cbfun):
    """
    
        Sets the iconify callback for the specified window.
    
        Wrapper for:
            GLFWwindowiconifyfun glfwSetWindowIconifyCallback(GLFWwindow* window, GLFWwindowiconifyfun cbfun);
        
    """
def set_window_maximize_callback(window, cbfun):
    """
    
            Sets the maximize callback for the specified window.
    
            Wrapper for:
                GLFWwindowmaximizefun glfwSetWindowMaximizeCallback(GLFWwindow* window, GLFWwindowmaximizefun cbfun);
            
    """
def set_window_monitor(window, monitor, xpos, ypos, width, height, refresh_rate):
    """
    
            Sets the mode, monitor, video mode and placement of a window.
    
            Wrapper for:
                void glfwSetWindowMonitor(GLFWwindow* window, GLFWmonitor* monitor, int xpos, int ypos, int width, int height, int refreshRate);
            
    """
def set_window_opacity(window, opacity):
    """
    
            Sets the opacity of the whole window.
    
            Wrapper for:
                void glfwSetWindowOpacity(GLFWwindow* window, float opacity);
            
    """
def set_window_pos(window, xpos, ypos):
    """
    
        Sets the position of the client area of the specified window.
    
        Wrapper for:
            void glfwSetWindowPos(GLFWwindow* window, int xpos, int ypos);
        
    """
def set_window_pos_callback(window, cbfun):
    """
    
        Sets the position callback for the specified window.
    
        Wrapper for:
            GLFWwindowposfun glfwSetWindowPosCallback(GLFWwindow* window, GLFWwindowposfun cbfun);
        
    """
def set_window_refresh_callback(window, cbfun):
    """
    
        Sets the refresh callback for the specified window.
    
        Wrapper for:
            GLFWwindowrefreshfun glfwSetWindowRefreshCallback(GLFWwindow* window, GLFWwindowrefreshfun cbfun);
        
    """
def set_window_should_close(window, value):
    """
    
        Sets the close flag of the specified window.
    
        Wrapper for:
            void glfwSetWindowShouldClose(GLFWwindow* window, int value);
        
    """
def set_window_size(window, width, height):
    """
    
        Sets the size of the client area of the specified window.
    
        Wrapper for:
            void glfwSetWindowSize(GLFWwindow* window, int width, int height);
        
    """
def set_window_size_callback(window, cbfun):
    """
    
        Sets the size callback for the specified window.
    
        Wrapper for:
            GLFWwindowsizefun glfwSetWindowSizeCallback(GLFWwindow* window, GLFWwindowsizefun cbfun);
        
    """
def set_window_size_limits(window, minwidth, minheight, maxwidth, maxheight):
    """
    
            Sets the size limits of the specified window.
    
            Wrapper for:
                void glfwSetWindowSizeLimits(GLFWwindow* window, int minwidth, int minheight, int maxwidth, int maxheight);
            
    """
def set_window_title(window, title):
    """
    
        Sets the title of the specified window.
    
        Wrapper for:
            void glfwSetWindowTitle(GLFWwindow* window, const char* title);
        
    """
def set_window_user_pointer(window, pointer):
    """
    
        Sets the user pointer of the specified window. You may pass a normal python object into this function and it will
        be wrapped automatically. The object will be kept in existence until the pointer is set to something else or
        until the window is destroyed.
    
        Wrapper for:
            void glfwSetWindowUserPointer(GLFWwindow* window, void* pointer);
        
    """
def set_x11_selection_string(string):
    """
    
            Sets the current primary selection to the specified string.
    
            Wrapper for:
                void glfwSetX11SelectionString(const char* string);
            
    """
def show_window(window):
    """
    
        Makes the specified window visible.
    
        Wrapper for:
            void glfwShowWindow(GLFWwindow* window);
        
    """
def swap_buffers(window):
    """
    
        Swaps the front and back buffers of the specified window.
    
        Wrapper for:
            void glfwSwapBuffers(GLFWwindow* window);
        
    """
def swap_interval(interval):
    """
    
        Sets the swap interval for the current context.
    
        Wrapper for:
            void glfwSwapInterval(int interval);
        
    """
def terminate():
    """
    
        Terminates the GLFW library.
    
        Wrapper for:
            void glfwTerminate(void);
        
    """
def update_gamepad_mappings(string):
    """
    
            Adds the specified SDL_GameControllerDB gamepad mappings.
    
            Wrapper for:
                int glfwUpdateGamepadMappings(const char* string);
            
    """
def vulkan_supported():
    """
    
            Returns whether the Vulkan loader has been found.
    
            Wrapper for:
                int glfwVulkanSupported(void);
            
    """
def wait_events():
    """
    
        Waits until events are pending and processes them.
    
        Wrapper for:
            void glfwWaitEvents(void);
        
    """
def wait_events_timeout(timeout):
    """
    
            Waits with timeout until events are queued and processes them.
    
            Wrapper for:
                void glfwWaitEventsTimeout(double timeout);
            
    """
def window_hint(hint, value):
    """
    
        Sets the specified window hint to the desired value.
    
        Wrapper for:
            void glfwWindowHint(int hint, int value);
        
    """
def window_hint_string(hint, value):
    """
    
            Sets the specified window hint to the desired value.
    
            Wrapper for:
                void glfwWindowHintString(int hint, const char* value);
            
    """
def window_should_close(window):
    """
    
        Checks the close flag of the specified window.
    
        Wrapper for:
            int glfwWindowShouldClose(GLFWwindow* window);
        
    """
ACCUM_ALPHA_BITS: int = 135178
ACCUM_BLUE_BITS: int = 135177
ACCUM_GREEN_BITS: int = 135176
ACCUM_RED_BITS: int = 135175
ALPHA_BITS: int = 135172
ANGLE_PLATFORM_TYPE: int = 327682
ANGLE_PLATFORM_TYPE_D3D11: int = 225285
ANGLE_PLATFORM_TYPE_D3D9: int = 225284
ANGLE_PLATFORM_TYPE_METAL: int = 225288
ANGLE_PLATFORM_TYPE_NONE: int = 225281
ANGLE_PLATFORM_TYPE_OPENGL: int = 225282
ANGLE_PLATFORM_TYPE_OPENGLES: int = 225283
ANGLE_PLATFORM_TYPE_VULKAN: int = 225287
ANY_PLATFORM: int = 393216
ANY_POSITION: int = 2147483648
ANY_RELEASE_BEHAVIOR: int = 0
API_UNAVAILABLE: int = 65542
ARROW_CURSOR: int = 221185
AUTO_ICONIFY: int = 131078
AUX_BUFFERS: int = 135179
BLUE_BITS: int = 135171
CENTER_CURSOR: int = 131081
CLIENT_API: int = 139265
COCOA_CHDIR_RESOURCES: int = 331777
COCOA_FRAME_NAME: int = 143362
COCOA_GRAPHICS_SWITCHING: int = 143363
COCOA_MENUBAR: int = 331778
COCOA_RETINA_FRAMEBUFFER: int = 143361
CONNECTED: int = 262145
CONTEXT_CREATION_API: int = 139275
CONTEXT_DEBUG: int = 139271
CONTEXT_NO_ERROR: int = 139274
CONTEXT_RELEASE_BEHAVIOR: int = 139273
CONTEXT_REVISION: int = 139268
CONTEXT_ROBUSTNESS: int = 139269
CONTEXT_VERSION_MAJOR: int = 139266
CONTEXT_VERSION_MINOR: int = 139267
CROSSHAIR_CURSOR: int = 221187
CURSOR: int = 208897
CURSOR_CAPTURED: int = 212996
CURSOR_DISABLED: int = 212995
CURSOR_HIDDEN: int = 212994
CURSOR_NORMAL: int = 212993
CURSOR_UNAVAILABLE: int = 65547
DECORATED: int = 131077
DEPTH_BITS: int = 135173
DISCONNECTED: int = 262146
DONT_CARE: int = -1
DOUBLEBUFFER: int = 135184
EGL_CONTEXT_API: int = 221186
ERROR_REPORTING: str = 'warn'
FALSE: int = 0
FEATURE_UNAVAILABLE: int = 65548
FEATURE_UNIMPLEMENTED: int = 65549
FLOATING: int = 131079
FOCUSED: int = 131073
FOCUS_ON_SHOW: int = 131084
FORMAT_UNAVAILABLE: int = 65545
GAMEPAD_AXIS_LAST: int = 5
GAMEPAD_AXIS_LEFT_TRIGGER: int = 4
GAMEPAD_AXIS_LEFT_X: int = 0
GAMEPAD_AXIS_LEFT_Y: int = 1
GAMEPAD_AXIS_RIGHT_TRIGGER: int = 5
GAMEPAD_AXIS_RIGHT_X: int = 2
GAMEPAD_AXIS_RIGHT_Y: int = 3
GAMEPAD_BUTTON_A: int = 0
GAMEPAD_BUTTON_B: int = 1
GAMEPAD_BUTTON_BACK: int = 6
GAMEPAD_BUTTON_CIRCLE: int = 1
GAMEPAD_BUTTON_CROSS: int = 0
GAMEPAD_BUTTON_DPAD_DOWN: int = 13
GAMEPAD_BUTTON_DPAD_LEFT: int = 14
GAMEPAD_BUTTON_DPAD_RIGHT: int = 12
GAMEPAD_BUTTON_DPAD_UP: int = 11
GAMEPAD_BUTTON_GUIDE: int = 8
GAMEPAD_BUTTON_LAST: int = 14
GAMEPAD_BUTTON_LEFT_BUMPER: int = 4
GAMEPAD_BUTTON_LEFT_THUMB: int = 9
GAMEPAD_BUTTON_RIGHT_BUMPER: int = 5
GAMEPAD_BUTTON_RIGHT_THUMB: int = 10
GAMEPAD_BUTTON_SQUARE: int = 2
GAMEPAD_BUTTON_START: int = 7
GAMEPAD_BUTTON_TRIANGLE: int = 3
GAMEPAD_BUTTON_X: int = 2
GAMEPAD_BUTTON_Y: int = 3
GREEN_BITS: int = 135170
HAND_CURSOR: int = 221188
HAT_CENTERED: int = 0
HAT_DOWN: int = 4
HAT_LEFT: int = 8
HAT_LEFT_DOWN: int = 12
HAT_LEFT_UP: int = 9
HAT_RIGHT: int = 2
HAT_RIGHT_DOWN: int = 6
HAT_RIGHT_UP: int = 3
HAT_UP: int = 1
HOVERED: int = 131083
HRESIZE_CURSOR: int = 221189
IBEAM_CURSOR: int = 221186
ICONIFIED: int = 131074
INVALID_ENUM: int = 65539
INVALID_VALUE: int = 65540
JOYSTICK_1: int = 0
JOYSTICK_10: int = 9
JOYSTICK_11: int = 10
JOYSTICK_12: int = 11
JOYSTICK_13: int = 12
JOYSTICK_14: int = 13
JOYSTICK_15: int = 14
JOYSTICK_16: int = 15
JOYSTICK_2: int = 1
JOYSTICK_3: int = 2
JOYSTICK_4: int = 3
JOYSTICK_5: int = 4
JOYSTICK_6: int = 5
JOYSTICK_7: int = 6
JOYSTICK_8: int = 7
JOYSTICK_9: int = 8
JOYSTICK_HAT_BUTTONS: int = 327681
JOYSTICK_LAST: int = 15
KEY_0: int = 48
KEY_1: int = 49
KEY_2: int = 50
KEY_3: int = 51
KEY_4: int = 52
KEY_5: int = 53
KEY_6: int = 54
KEY_7: int = 55
KEY_8: int = 56
KEY_9: int = 57
KEY_A: int = 65
KEY_APOSTROPHE: int = 39
KEY_B: int = 66
KEY_BACKSLASH: int = 92
KEY_BACKSPACE: int = 259
KEY_C: int = 67
KEY_CAPS_LOCK: int = 280
KEY_COMMA: int = 44
KEY_D: int = 68
KEY_DELETE: int = 261
KEY_DOWN: int = 264
KEY_E: int = 69
KEY_END: int = 269
KEY_ENTER: int = 257
KEY_EQUAL: int = 61
KEY_ESCAPE: int = 256
KEY_F: int = 70
KEY_F1: int = 290
KEY_F10: int = 299
KEY_F11: int = 300
KEY_F12: int = 301
KEY_F13: int = 302
KEY_F14: int = 303
KEY_F15: int = 304
KEY_F16: int = 305
KEY_F17: int = 306
KEY_F18: int = 307
KEY_F19: int = 308
KEY_F2: int = 291
KEY_F20: int = 309
KEY_F21: int = 310
KEY_F22: int = 311
KEY_F23: int = 312
KEY_F24: int = 313
KEY_F25: int = 314
KEY_F3: int = 292
KEY_F4: int = 293
KEY_F5: int = 294
KEY_F6: int = 295
KEY_F7: int = 296
KEY_F8: int = 297
KEY_F9: int = 298
KEY_G: int = 71
KEY_GRAVE_ACCENT: int = 96
KEY_H: int = 72
KEY_HOME: int = 268
KEY_I: int = 73
KEY_INSERT: int = 260
KEY_J: int = 74
KEY_K: int = 75
KEY_KP_0: int = 320
KEY_KP_1: int = 321
KEY_KP_2: int = 322
KEY_KP_3: int = 323
KEY_KP_4: int = 324
KEY_KP_5: int = 325
KEY_KP_6: int = 326
KEY_KP_7: int = 327
KEY_KP_8: int = 328
KEY_KP_9: int = 329
KEY_KP_ADD: int = 334
KEY_KP_DECIMAL: int = 330
KEY_KP_DIVIDE: int = 331
KEY_KP_ENTER: int = 335
KEY_KP_EQUAL: int = 336
KEY_KP_MULTIPLY: int = 332
KEY_KP_SUBTRACT: int = 333
KEY_L: int = 76
KEY_LAST: int = 348
KEY_LEFT: int = 263
KEY_LEFT_ALT: int = 342
KEY_LEFT_BRACKET: int = 91
KEY_LEFT_CONTROL: int = 341
KEY_LEFT_SHIFT: int = 340
KEY_LEFT_SUPER: int = 343
KEY_M: int = 77
KEY_MENU: int = 348
KEY_MINUS: int = 45
KEY_N: int = 78
KEY_NUM_LOCK: int = 282
KEY_O: int = 79
KEY_P: int = 80
KEY_PAGE_DOWN: int = 267
KEY_PAGE_UP: int = 266
KEY_PAUSE: int = 284
KEY_PERIOD: int = 46
KEY_PRINT_SCREEN: int = 283
KEY_Q: int = 81
KEY_R: int = 82
KEY_RIGHT: int = 262
KEY_RIGHT_ALT: int = 346
KEY_RIGHT_BRACKET: int = 93
KEY_RIGHT_CONTROL: int = 345
KEY_RIGHT_SHIFT: int = 344
KEY_RIGHT_SUPER: int = 347
KEY_S: int = 83
KEY_SCROLL_LOCK: int = 281
KEY_SEMICOLON: int = 59
KEY_SLASH: int = 47
KEY_SPACE: int = 32
KEY_T: int = 84
KEY_TAB: int = 258
KEY_U: int = 85
KEY_UNKNOWN: int = -1
KEY_UP: int = 265
KEY_V: int = 86
KEY_W: int = 87
KEY_WORLD_1: int = 161
KEY_WORLD_2: int = 162
KEY_X: int = 88
KEY_Y: int = 89
KEY_Z: int = 90
LOCK_KEY_MODS: int = 208900
LOSE_CONTEXT_ON_RESET: int = 200706
MAXIMIZED: int = 131080
MOD_ALT: int = 4
MOD_CAPS_LOCK: int = 16
MOD_CONTROL: int = 2
MOD_NUM_LOCK: int = 32
MOD_SHIFT: int = 1
MOD_SUPER: int = 8
MOUSE_BUTTON_1: int = 0
MOUSE_BUTTON_2: int = 1
MOUSE_BUTTON_3: int = 2
MOUSE_BUTTON_4: int = 3
MOUSE_BUTTON_5: int = 4
MOUSE_BUTTON_6: int = 5
MOUSE_BUTTON_7: int = 6
MOUSE_BUTTON_8: int = 7
MOUSE_BUTTON_LAST: int = 7
MOUSE_BUTTON_LEFT: int = 0
MOUSE_BUTTON_MIDDLE: int = 2
MOUSE_BUTTON_RIGHT: int = 1
MOUSE_PASSTHROUGH: int = 131085
NATIVE_CONTEXT_API: int = 221185
NORMALIZE_GAMMA_RAMPS: bool = True
NOT_ALLOWED_CURSOR: int = 221194
NOT_INITIALIZED: int = 65537
NO_API: int = 0
NO_CURRENT_CONTEXT: int = 65538
NO_ERROR: int = 0
NO_RESET_NOTIFICATION: int = 200705
NO_ROBUSTNESS: int = 0
NO_WINDOW_CONTEXT: int = 65546
OPENGL_ANY_PROFILE: int = 0
OPENGL_API: int = 196609
OPENGL_COMPAT_PROFILE: int = 204802
OPENGL_CORE_PROFILE: int = 204801
OPENGL_DEBUG_CONTEXT: int = 139271
OPENGL_ES_API: int = 196610
OPENGL_FORWARD_COMPAT: int = 139270
OPENGL_PROFILE: int = 139272
OSMESA_CONTEXT_API: int = 221187
OUT_OF_MEMORY: int = 65541
PLATFORM: int = 327683
PLATFORM_COCOA: int = 393218
PLATFORM_ERROR: int = 65544
PLATFORM_NULL: int = 393221
PLATFORM_UNAVAILABLE: int = 65550
PLATFORM_WAYLAND: int = 393219
PLATFORM_WIN32: int = 393217
PLATFORM_X11: int = 393220
POINTING_HAND_CURSOR: int = 221188
POSITION_X: int = 131086
POSITION_Y: int = 131087
PRESS: int = 1
RAW_MOUSE_MOTION: int = 208901
RED_BITS: int = 135169
REFRESH_RATE: int = 135183
RELEASE: int = 0
RELEASE_BEHAVIOR_FLUSH: int = 217089
RELEASE_BEHAVIOR_NONE: int = 217090
REPEAT: int = 2
RESIZABLE: int = 131075
RESIZE_ALL_CURSOR: int = 221193
RESIZE_EW_CURSOR: int = 221189
RESIZE_NESW_CURSOR: int = 221192
RESIZE_NS_CURSOR: int = 221190
RESIZE_NWSE_CURSOR: int = 221191
SAMPLES: int = 135181
SCALE_FRAMEBUFFER: int = 139277
SCALE_TO_MONITOR: int = 139276
SRGB_CAPABLE: int = 135182
STENCIL_BITS: int = 135174
STEREO: int = 135180
STICKY_KEYS: int = 208898
STICKY_MOUSE_BUTTONS: int = 208899
TRANSPARENT_FRAMEBUFFER: int = 131082
TRUE: int = 1
VERSION_MAJOR: int = 3
VERSION_MINOR: int = 4
VERSION_REVISION: int = 0
VERSION_UNAVAILABLE: int = 65543
VISIBLE: int = 131076
VRESIZE_CURSOR: int = 221190
WAYLAND_APP_ID: int = 155649
WAYLAND_DISABLE_LIBDECOR: int = 229378
WAYLAND_LIBDECOR: int = 339969
WAYLAND_PREFER_LIBDECOR: int = 229377
WIN32_KEYBOARD_MENU: int = 151553
WIN32_SHOWDEFAULT: int = 151554
X11_CLASS_NAME: int = 147457
X11_INSTANCE_NAME: int = 147458
X11_XCB_VULKAN_SURFACE: int = 335873
_PREVIEW: bool = False
__author__: str = 'Florian Rhiem (florian.rhiem@gmail.com)'
__copyright__: str = 'Copyright (c) 2013-2024 Florian Rhiem'
__license__: str = 'MIT'
__version__: str = '2.8.0'
_allocate_callback = None
_callback_repositories: list = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
_char_callback_repository: dict = {}
_cursor_enter_callback_repository: dict = {}
_cursor_pos_callback_repository: dict = {}
_deallocate_callback = None
_default_error_callback: ctypes.CFUNCTYPE.<locals>.CFunctionType  # value = <CFunctionType object>
_error_callback: tuple  # value = (_handle_glfw_errors, <CFunctionType object>)
_exc_info_from_callback = None
_framebuffer_size_callback_repository: dict = {}
_glfw: ctypes.CDLL  # value = <CDLL '/usr/lib/libglfw.so.3.4', handle 294ff860 at 0x7ef23226e720>
_joystick_callback = None
_joystick_user_data_repository: dict = {}
_key_callback_repository: dict = {}
_loader_callback = None
_monitor_callback = None
_monitor_user_data_repository: dict = {}
_mouse_button_callback_repository: dict = {}
_reallocate_callback = None
_scroll_callback_repository: dict = {}
_window_char_mods_callback_repository: dict = {}
_window_close_callback_repository: dict = {}
_window_content_scale_callback_repository: dict = {}
_window_drop_callback_repository: dict = {}
_window_focus_callback_repository: dict = {}
_window_iconify_callback_repository: dict = {}
_window_maximize_callback_repository: dict = {}
_window_pos_callback_repository: dict = {}
_window_refresh_callback_repository: dict = {}
_window_size_callback_repository: dict = {}
_window_user_data_repository: dict = {}
division: __future__._Feature  # value = _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 131072)
print_function: __future__._Feature  # value = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 1048576)
unicode_literals: __future__._Feature  # value = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 2097152)
