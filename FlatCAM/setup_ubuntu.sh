#!/bin/sh -e

# Ubuntu packages

sudo apt-get install -y \
	libfreetype6 \
	libfreetype6-dev \
	libgeos-dev \
	libpng-dev \
	libspatialindex-dev \
	qt5-style-plugins \
	python3-dev \
	python3-gdal \
	python3-pip \
	python3-pyqt5 \
	python3-pyqt5.qtopengl \
	python3-simplejson \
	python3-tk \
	python3-reportlab \
	python3-svglib \
	python3-vispy \
	python3-opengl \
	python3-ezdxf \
	python3-ortools \
	python3-protobuf \
	python3-qrcode


# Python packages

sudo -H python3 -m pip install -r requirements.txt
