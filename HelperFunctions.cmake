#Sets the RUNTIME_DLL_PATHS property for a given target
#Used to store the paths of runtime dependencies for a given target output
#target: name of source target
#deps_list: list of absolute paths to dependency .dll files
function(set_runtime_dll_paths target deps_list)
	set_property(TARGET ${target} PROPERTY RUNTIME_DLL_PATHS ${deps_list})
endfunction()

#Copies the dependencies from a source target's RUNTIME_DLL_PATHS to an output path
#RUNTIME_DLL_PATHS is set in the source target's CMakeLists.txt with set_runtime_dll_paths
#src_target: a target with dependencies
#dest_target: a target that uses the src_target; the dependency copies will trigger on this target POST_BUILD
#dest_path: a path to an executable that links to the src_target
function(install_runtime_dlls src_target dest_target dest_path)
    add_custom_command(TARGET ${dest_target} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_RUNTIME_DLLS:${src_target}> ${dest_path} COMMAND_EXPAND_LISTS)
    get_target_property(src_dependency_paths ${src_target} RUNTIME_DLL_PATHS)
    set(dependency_list ${src_dependency_paths})
    foreach(path ${dependency_list})
        add_custom_command(TARGET ${dest_target} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy ${path} ${dest_path})
    endforeach()
endfunction()
