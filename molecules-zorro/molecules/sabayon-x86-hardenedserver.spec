# use abs path, otherwise daily iso build automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/hardenedserver.common

%env release_version: ${SABAYON_RELEASE:-11}
release_desc: x86 Hardened Server

# pre chroot command, example, for 32bit chroots on 64bit system, you always
# have to append "linux32" this is useful for inner_chroot_script
prechroot: linux32

# Path to source ISO file (MANDATORY)
%env source_iso: ${SABAYON_MOLECULE_HOME:-/sabayon}/iso/Sabayon_Linux_DAILY_x86_SpinBase.iso

# Destination ISO image name, call whatever you want.iso, not mandatory
%env destination_iso_image_name: Sabayon_Linux_${SABAYON_RELEASE:-11}_x86_HardenedServer.iso
