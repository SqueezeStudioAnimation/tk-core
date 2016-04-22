# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Constants relating to the app/engine part of the Tank Stack.

(for constants relating to the low level part of the tank stack, see ..constants)

"""

# metadata file for engines and apps
BUNDLE_METADATA_FILE = "info.yml"

# Valid data types for use in app/engine settings schemas
TANK_SCHEMA_VALID_TYPES = [
    "str",
    "int",
    "float",
    "bool",
    "list",
    "dict",
    "tank_type",
    "template",
    "hook",
    "shotgun_entity_type",
    "shotgun_permission_group",
    "shotgun_filter",
    "config_path"
]

# Types from the list above that expect "str" values.
TANK_SCHEMA_STRING_TYPES = [
    "tank_type",
    "template",
    "hook",
    "shotgun_entity_type",
    "shotgun_permission_group",
    "config_path"
]

# a folder to look for an automatically add to the pythonpath
BUNDLE_PYTHON_FOLDER = "python"

# app store approvals mode
APP_STORE_QA_MODE_ENV_VAR = "TANK_QA_ENABLED"

# force use old, non-structure preseving parser
USE_LEGACY_YAML_ENV_VAR = "TK_USE_LEGACY_YAML"

# flag to pass for legacy yaml parser
LEGACY_YAML_PARSER_FLAG = "--use-legacy-yaml"

# the file to look for that defines and bootstraps an engine
ENGINE_FILE = "engine.py"

# inside the engine location, the folder in which to look for apps
ENGINE_APPS_LOCATION = "apps"

# app settings location
ENGINE_APP_SETTINGS_LOCATION = "app_settings"

# inside the engine config location, the folder in which to look for environments
ENGINE_ENV_LOCATIONS = "env"

# the key in the configuration for an engine which holds the environment
ENGINE_CONFIG_ENVIRONMENT_KEY = "environment"

# hook that is executed when a tank instance initializes.
TANK_INIT_HOOK_NAME = "tank_init"

# hook that is executed whenever an engine has initialized
TANK_ENGINE_INIT_HOOK_NAME = "engine_init"

# hook that is executed whenever a bundle has initialized
TANK_BUNDLE_INIT_HOOK_NAME = "bundle_init"

# hook to be executed after bundle install
BUNDLE_POST_INSTALL_HOOK = "post_install.py"

# metrics logging custom hooks blacklist
TANK_LOG_METRICS_CUSTOM_HOOK_BLACKLIST = [
    "pick_environment",
]

# flag to indicate that an app command is a legacy style
# shotgun multi select action
LEGACY_MULTI_SELECT_ACTION_FLAG = "shotgun_multi_select_action"

# hook that is executed whenever a PipelineConfiguration instance initializes.
PIPELINE_CONFIGURATION_INIT_HOOK_NAME = "pipeline_configuration_init"

# hook that is executed whenever a cache location should be determined
CACHE_LOCATION_HOOK_NAME = "cache_location"

# the name of the file that holds the inverse root defs
# note - this is no longer used by the core itself, but it is still
# being used by the perforce integration to handle
# back tracking. The perforce code requests this constant directly
# from its code.
CONFIG_BACK_MAPPING_FILE = "tank_configs.yml"

# default value for hooks
TANK_BUNDLE_DEFAULT_HOOK_SETTING = "default"

# the key name used to identify default values in a manifest file. used as both
# the actual key as well as the prefix for engine-specific default value keys.
# example: "default_value_tk-maya".
TANK_SCHEMA_DEFAULT_VALUE_KEY = "default_value"

# default method to execute on hooks
DEFAULT_HOOK_METHOD = "execute"

# if the engine name is included in a hook definition, include this in the manifest.
TANK_HOOK_ENGINE_REFERENCE_TOKEN = "{engine_name}"

# hooks that are used during folder creation.
PROCESS_FOLDER_CREATION_HOOK_NAME = "process_folder_creation"

# hook to choose the environment file given a context
PICK_ENVIRONMENT_CORE_HOOK_NAME = "pick_environment"

# the configuration key inside an environment which holds all the app configs
ENVIRONMENT_CFG_APPS_SECTION = "apps"

# the key that holds the app descriptor dict
ENVIRONMENT_LOCATION_KEY = "location"

# the file to look for that defines and bootstraps an app
APP_FILE = "app.py"

# an optional stylesheet that can be defined by bundles
BUNDLE_STYLESHEET_FILE = "style.qss"

# define our standard stylesheet constants 
SG_STYLESHEET_CONSTANTS = { "SG_HIGHLIGHT_COLOR": "#18A7E3",
                            "SG_ALERT_COLOR": "#FC6246",
                            "SG_FOREGROUND_COLOR": "#C8C8C8"}

# the storage name that is treated to be the primary storage for tank
PRIMARY_STORAGE_NAME = "primary"

# the file to look for that defines and bootstraps a framework
FRAMEWORK_FILE = "framework.py"

# the name of the primary pipeline configuration
PRIMARY_PIPELINE_CONFIG_NAME = "Primary"
UNMANAGED_PIPELINE_CONFIG_NAME = "Unmanaged"

# special dev descriptor token that can be used
# as a replacement for the path to a pipeline configuration
PIPELINE_CONFIG_DEV_DESCRIPTOR_TOKEN = "{PIPELINE_CONFIG}"

# Configuration file containing setup and path details
PIPELINECONFIG_FILE = "pipeline_configuration.yml"

# app store: the entity that represents the core api
TANK_CORE_VERSION_ENTITY = "CustomNonProjectEntity01"

# app store: the entity representing configs
TANK_CONFIG_ENTITY = "CustomNonProjectEntity07"

# app store: the entity representing config versions
TANK_CONFIG_VERSION_ENTITY = "CustomNonProjectEntity08"

# app store: the field containing the zip payload
TANK_CODE_PAYLOAD_FIELD = "sg_payload"

# app store: dummy project required when writing event data to the system
TANK_APP_STORE_DUMMY_PROJECT = {"type": "Project", "id": 64}

# Shotgun: The entity that represents Pipeline Configurations in Shotgun
PIPELINE_CONFIGURATION_ENTITY = "PipelineConfiguration"

# The name of the default config
DEFAULT_CFG = "tk-config-default"

# the name of the shell engine
SHELL_ENGINE = "tk-shell"

# valid characters for a template key name
TEMPLATE_KEY_NAME_REGEX = "[a-zA-Z_ 0-9\.]+"

# a human readable explanation of the above. For error messages.
VALID_TEMPLATE_KEY_NAME_DESC = "letters, numbers, underscore, space and period"

# the name of the file that holds the templates.yml config
CONTENT_TEMPLATES_FILE = "templates.yml"

# the name of the file that contains the storage root definitions
STORAGE_ROOTS_FILE = "roots.yml"

# the name of the include section in env and template files
SINGLE_INCLUDE_SECTION = "include"

# the name of the includes section in env and template files
MULTI_INCLUDE_SECTION = "includes"

# the key sections in a template file
TEMPLATE_SECTIONS = ["keys", "paths", "strings"]

# the path section in a templates file
TEMPLATE_PATH_SECTION = "paths"

# the string section in a templates file
TEMPLATE_STRING_SECTION = "strings"

# the shotgun engine always has this name
SHOTGUN_ENGINE_NAME = "tk-shotgun"

# the menu favourites key for an engine
MENU_FAVOURITES_KEY = "menu_favourites"



# init cache for fast initialization
SITE_INIT_CACHE_FILE_NAME = "toolkit_init.cache"

# the location of the toolkit app store
SGTK_APP_STORE = "https://tank.shotgunstudio.com"

# name of the app store specific proxy setting
APP_STORE_HTTP_PROXY = "app_store_http_proxy"
