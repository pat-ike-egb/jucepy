cmake_minimum_required(VERSION 3.10)
project(jucepy)

include(cmake/download_cpm.cmake)

CPMAddPackage("gh:pybind/pybind11#master")
CPMAddPackage("gh:juce-framework/JUCE#develop")

find_package( CURL REQUIRED )

# # Link dependencies
# target_link_libraries( DAWPP PRIVATE CURL::libcurl )
# target_link_libraries( DAWPP PRIVATE juce_core )
# target_link_libraries( DAWPP PRIVATE juce_audio_basics )

