#This is the top-level Monorepo C++ CMakeLists.txt file
#Users should invoke this CMake file instead of building from within a module
#New modules MUST be buildable using this CMake file
cmake_minimum_required(VERSION 3.15)

project(gui-monorepo)

if(${CMAKE_SYSTEM_NAME} STREQUAL "Linux")
	set(LINUX 1)
	if(NOT CMAKE_BUILD_TYPE)
		set(CMAKE_BUILD_TYPE Debug)
	endif()
endif()

include(FetchContent)
FetchContent_Declare(
        googletest
        GIT_REPOSITORY    https://github.com/google/googletest.git
        GIT_TAG           release-1.12.1
)


#Force google test to use the project setting for the MSVC C library setting
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
enable_testing()

#option(CONDA_CONFIG_ENV "Name of the conda env config file to use")
##Target to pull in conda dependencies
# if(CONDA_CONFIG_ENV)
#     include(FindPythonInterp)
#     set(CONDA_DEPENDENCIES_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/conda_dependencies")
 
#     execute_process(
#       COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/bin/dependency_installer.py
#       -o ${CONDA_DEPENDENCIES_DIRECTORY}
#       -e ${CONDA_CONFIG_ENV}
#       ${CONDA_ADDITIONAL_ARGS})
    
#     #Add installed dependencies to Cmake search path
#     if(APPLE OR LINUX)
#         list(PREPEND CMAKE_PREFIX_PATH ${CONDA_DEPENDENCIES_DIRECTORY})
#     elseif(MSVC)
#         list(PREPEND CMAKE_PREFIX_PATH ${CONDA_DEPENDENCIES_DIRECTORY}/Library)
#     endif()
# endif()

include(HelperFunctions.cmake)

#Options for which modules to build
#Pass to CMake command lines through -DBUIILD_{MODULE}=ON

option(BUILD_PLUGIN_GUI "Build Open Ephys Plugin GUI")
option(BUILD_DATA_SNAPSHOT "Build Data Snapshot Plugin")

#Check definitions of module arguments and add necessary module directories

## Example of platform-specific plugin:
#if(MSVC)
#if(BUILD_NIDAQ)
#    add_subdirectory(nidaq-plugin)
#endif()
#endif()

if(BUILD_PLUGIN_GUI)
    add_subdirectory(plugin-GUI)
endif()

if(BUILD_DATA_SNAPSHOT)
    add_subdirectory(plugins/data-snapshot)
endif()